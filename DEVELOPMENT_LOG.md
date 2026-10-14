# Utvecklingslogg

Projekt: AI som känner igen enkla objekt via kamera
Teknik: Python, OpenCV, YOLO (förtränad modell)

## 16 September 2026
**Vad jag gjorde:**
Jag satte igång projektet från början. Jag installerade biblioteken OpenCV och
ultralytics (som innehåller YOLO) och skrev den första versionen av programmet
i `main.py`. Programmet öppnar kameran, kör YOLO på varje bildruta och ritar ut
rutor med objektets namn och konfidens, plus FPS i hörnet. Jag skrev också en
testplan i `TESTPLAN.md` och en mall för resultaten i `test_results.csv`.

**Vad jag lärde mig:**
Jag lärde mig att ultralytics laddar ner den förtränade modellen `yolov8n.pt`
automatiskt första gången programmet körs. Modellen känner igen 80 olika typer
av objekt, t.ex. person, kopp och flaska. Jag lärde mig också att jag kan
ställa in en konfidensgräns (jag valde 0,40) så att programmet inte visar
osäkra detektioner.

**Problem/lösning:**
Första problemet var att installationen av PyTorch tog lång tid, så jag fick
köra den i bakgrunden och vänta. Ett annat problem var att kameran tog flera
sekunder att öppna; jag löste det med `cv2.CAP_DSHOW` i Windows. Jag mätte att
modellen tar ungefär 64 ms per bild på min dator, vilket motsvarar ungefär 16
FPS. Med kameran igång mätte jag 18,5 FPS, så realtid fungerar.

**Nästa steg:**
Köra programmet med kameran och göra testerna i `TESTPLAN.md` (olika objekt,
avstånd och belysning) och fylla i resultaten i `test_results.csv`.
