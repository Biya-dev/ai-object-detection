# AI som känner igen enkla objekt via kamera

Python-program som använder datorns kamera och en förtränad YOLO-modell för att
upptäcka enkla objekt i realtid. Programmet ritar en ruta runt varje objekt och
visar objektets namn och hur säker modellen är (konfidens).

## Så kör jag programmet

1. Installera biblioteken:

   ```
   pip install -r requirements.txt
   ```

2. Starta programmet:

   ```
   python main.py
   ```

   Vid första körningen laddas den förtränade modellen `yolov8n.pt` ner
   automatiskt (den är gratis).

3. Styrning i programmet:
   - `q` = avsluta
   - `s` = spara en skärmbild (används som bevis vid testningen)
   - `r` = logga detektionerna (namn + konfidens) till `test_results.csv`

## Hur programmet fungerar

Kamera → OpenCV läser bild → YOLO upptäcker objekt → rutor med namn och
konfidens ritas på bilden → detta upprepas hela tiden (realtid).

## Filer

| Fil                | Vad den innehåller                              |
|--------------------|-------------------------------------------------|
| `main.py`          | Själva programmet                                |
| `requirements.txt` | Bibliotek som behövs                             |
| `TESTPLAN.md`      | Min testplan för skolrapporten                   |
| `test_results.csv` | Mall där jag fyller i testresultat               |
| `DEVELOPMENT_LOG.md` | Min utvecklingslogg med problem och lösningar  |

## Teknik

- Python
- OpenCV (kamera och bildvisning)
- YOLO via biblioteket `ultralytics`
- Förtränad modell: YOLOv8n (tränad på COCO-datasetet med 80 olika objektklasser)
