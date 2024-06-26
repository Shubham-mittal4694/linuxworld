#!/usr/bin/env python3

import cgi
import cv2

print("Content-Type: text/html\n")

def show_two_cameras_in_one_frame(camera1_index, camera2_index):
    # Open the first camera
    cap1 = cv2.VideoCapture(camera1_index)
    # Open the second camera
    cap2 = cv2.VideoCapture(camera2_index)

    if not cap1.isOpened():
        print(f"<p>Cannot open camera {camera1_index}</p>")
        return
    if not cap2.isOpened():
        print(f"<p>Cannot open camera {camera2_index}</p>")
        return

    while True:
        # Capture frame-by-frame from both cameras
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("<p>Can't receive frame (stream end?). Exiting ...</p>")
            break

        # Resize frames if necessary to make them the same size
        height = max(frame1.shape[0], frame2.shape[0])
        width = frame1.shape[1] + frame2.shape[1]

        # Create a combined frame
        combined_frame = cv2.hconcat([frame1, frame2])

        # Display the resulting frame
        cv2.imshow('Combined Frame', combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture and close windows
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

# Example usage
form = cgi.FieldStorage()
camera1_index = int(form.getvalue("camera1_index", 0))
camera2_index = int(form.getvalue("camera2_index", 1))

print("<html><body>")
print("<h1>Combined Camera Feed</h1>")
show_two_cameras_in_one_frame(camera1_index, camera2_index)
print("</body></html>")
