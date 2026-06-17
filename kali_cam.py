import cv2
import face_recognition
import numpy as np
import requests
import time

#print("Kali Cam starting... stand clear for 30 seconds!")
time.sleep(30)
#print("Armed and watching...")

known_encodings = []
known_names = []

jeff_image = face_recognition.load_image_file("jeff.jpg")
jeff_encoding = face_recognition.face_encodings(jeff_image)[0]
known_encodings.append(jeff_encoding)
known_names.append("Jeff")

video_capture = cv2.VideoCapture(2)
ret, prev_frame = video_capture.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    motion = cv2.countNonZero(thresh)

    if motion > 50000:
        #print("Motion Detected! Checking Faces...")
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"
            if True in matches:
                name = known_names[matches.index(True)]
            if name == "Unknown":
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                cv2.imwrite(f"unknown_{timestamp}.jpg", frame)
                #print(f"Photo saved as unknown_{timestamp}.jpg")
                requests.post("https://ntfy.sh/jeffskalicam",
                              data="Unknown face detected!",
                              headers={"Title": "Kali Cam Alert"})
                #print("Alert Sent!")
                time.sleep(60)
    prev_gray = gray
    time.sleep(0.1)
    # cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    # cv2.putText(frame, name, (left, top-10), 0, 0.75, (0,255,0), 2)

    # cv2.imshow('Face Recognition', frame)

    # if cv2.waitKey(1) & 0xff == ord('q'):
    # break

video_capture.release()
# cv2.destroyAllWindows()
