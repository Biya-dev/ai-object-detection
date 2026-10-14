"""
AI som känner igen enkla objekt via kamera.

Programmet öppnar datorns kamera, använder en förtränad YOLO-modell
för att upptäcka objekt i realtid och ritar ut ruta, objektnamn
och konfidens på bilden.

Styrning:
    q = avsluta programmet
    s = spara en skärmbild (används vid testning)
    r = logga detektionerna till test_results.csv (används vid testning)

Utbildningsprojekt, Tillämpad programmering.
"""

import csv
import os
import time

import cv2
from ultralytics import YOLO

# Konfidensgräns: visa bara objekt där modellen är minst så här säker.
# 0,25 är Ultralytics standardvärde och visar även svagare detektioner.
CONFIDENCE_THRESHOLD = 0.25

# Upplösning som efterfrågas från kameran (min kamera stöder 1280x720).
# Högre upplösning gör att små och avlägsna objekt syns tydligare.
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# Upplösning som YOLO använder vid detektionen. Högre värde hittar mindre
# objekt men tar längre tid. 960 gav fler detektioner i mina mätningar
# utan att programmet blev märkbart långsammare.
IMG_SIZE = 960

# Förtränad YOLO-modell (laddas ner automatiskt vid första körningen)
MODEL_NAME = "yolov8n.pt"

# Kamera 0 = datorns inbyggda/anslutna kamera
CAMERA_INDEX = 0

# Resultatfil för testningen (fylls i manuellt: objekt, avstånd, belysning)
RESULTS_FILE = "test_results.csv"
RESULTS_HEADER = [
    "tidpunkt", "objekt", "upptackt_klass", "upptackt",
    "konfidens", "avstand_m", "belysning", "anteckningar",
]


def log_detections(detections: list) -> None:
    """Skriver en rad per upptäckt objekt till resultatfilen.

    detections: lista med (namn, konfidens) från den senaste bilden.
    Kolumnerna objekt, avstand_m, belysning och anteckningar lämnas
    tomma – jag fyller i dem manuellt efteråt.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(RESULTS_FILE) and os.path.getsize(RESULTS_FILE) > 0

    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(RESULTS_HEADER)

        if detections:
            for name, confidence in detections:
                writer.writerow([timestamp, "", name, "ja", f"{confidence:.2f}", "", "", ""])
                print(f"Loggad: {name} {confidence:.2f}")
        else:
            writer.writerow([timestamp, "", "", "nej", "", "", "", ""])
            print("Loggad: inga objekt upptäckta (upptackt = nej)")


def main() -> None:
    model = YOLO(MODEL_NAME)
    print(f"Modellen '{MODEL_NAME}' är laddad.")

    # CAP_DSHOW gör att kameran öppnas snabbare i Windows
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    if not cap.isOpened():
        raise RuntimeError("Kunde inte öppna kameran. Kontrollera att en kamera är ansluten.")

    # Be kameran om 1280x720 i stället för standard 640x480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    print("Kameran är öppen. 'q' = avsluta, 's' = spara bild, 'r' = logga resultat.")

    prev_time = time.time()
    fps = 0.0

    while True:
        ok, frame = cap.read()
        if not ok:
            print("Förlorade bildsignalen från kameran. Avslutar.")
            break

        # Kör YOLO på hela bilden
        results = model(frame, conf=CONFIDENCE_THRESHOLD, imgsz=IMG_SIZE)

        # Rita egna rutor med namn + konfidens
        annotated = frame.copy()
        detections = []  # (namn, konfidens) för loggning med 'r'
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls[0])
            name = results[0].names[class_id]
            confidence = float(box.conf[0])
            detections.append((name, confidence))

            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{name} {confidence:.2f}"
            cv2.putText(
                annotated, label, (x1, max(y1 - 8, 15)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,
            )

        # Räkna ut FPS (bilder per sekund)
        now = time.time()
        fps = 0.9 * fps + 0.1 * (1.0 / max(now - prev_time, 1e-6))
        prev_time = now
        cv2.putText(
            annotated, f"FPS: {fps:.1f}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
        )

        cv2.imshow("Objektigenkanning (YOLO)", annotated)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        if key == ord("s"):
            filename = time.strftime("screenshot_%Y%m%d_%H%M%S.png")
            cv2.imwrite(filename, annotated)
            print(f"Sparade bild: {filename}")
        if key == ord("r"):
            log_detections(detections)

    cap.release()
    cv2.destroyAllWindows()
    print("Programmet avslutades.")


if __name__ == "__main__":
    main()
