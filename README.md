# kali_cam
Facial recognition security camera with motion detection and push notifications
 A lightweight facial recognition security camera built with Python, OPenCV
 and face_recognition. Detects motion, identifies known faces, and sends
 push notifications via ntfy.sh for unknown visitors.

 ## Features
 - Motion triggered face detection
 - Known face recognition
 - Push notifications via ntfy.sh
 - Headless operation
 - Runs as a systemd service at boot
 - Runs in silent mode without warnings

  ## Harware
  - Any UVC compatible webcam (tested with Logitech C170)
  - Any Linux machine (developed on Kali Linux)

  ## Dependencies
  - Python 3
  - OpenCV
  - face_recognition
  - requests

  ## Philosophy 
  Built open source because they can't steal what you're giving away.

  ## Setup
  1. Take a photo of each known person and save as a .jpg
  2. Edit kali_cam.py and replace "jeff.jpg" with your photo file name
  3. Replace "Jeff" with the person's name
  4. Replace "jeffskalicam" with your ntfy.sh topic name
  5. Run: python3 kali_cam.py
  6. If you want to print warnings uncomment all the print statements
  7. The head display has been commented out as well and was left in to uncomment if needed for debugging purposes
