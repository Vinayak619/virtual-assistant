import cv2
import os
from datetime import datetime

def take_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Could not access the camera."

    ret, frame = cap.read()

    if ret:
        if not os.path.exists("photos"):
            os.makedirs("photos")

        filename = datetime.now().strftime("photos/photo_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        cap.release()
        return f"Photo taken and saved as {os.path.basename(filename)}"
    else:
        cap.release()
        return "Failed to capture image."
