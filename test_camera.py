"""
Litet testprogram som kollar om kameran fungerar.

Kör så här:  python test_camera.py
Om det står "fungerar" kan main.py använda kameran.
"""

import time

import cv2

CAMERA_INDEX = 0

start = time.time()

# CAP_DSHOW gör att kameran öppnas snabbare i Windows
cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

if not cap.isOpened():
    print(f"Kamera {CAMERA_INDEX}: GICK INTE ATT ÖPPNA.")
else:
    ok, frame = cap.read()
    cap.release()
    if ok:
        height, width = frame.shape[:2]
        print(f"Kamera {CAMERA_INDEX} fungerar. Bildstorlek: {width}x{height}. "
              f"Testet tog {time.time() - start:.1f} sekunder.")
    else:
        print(f"Kamera {CAMERA_INDEX} öppnades men gav ingen bild.")
