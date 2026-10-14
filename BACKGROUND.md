# Projektbakgrund

I detta projekt bygger jag ett Pythonprogram som använder datorns kamera och en
förtränad YOLO-modell för att känna igen enkla objekt i realtid. Programmet visar
objektets namn, hur säker modellen är (konfidens) och ritar en ruta runt objektet.
I den här bakgrunden beskriver jag den teori som ligger bakom projektet och
kopplar det till mitt gymnasiearbete.

## Artificiell intelligens (AI)

Artificiell intelligens, eller AI, är ett samlingsnamn för teknologier som försöker
få datorprogram att fungera mer likt en människa. Enligt Internetkunskap handlar
det bland annat om att kunna lära sig av data och att känna igen mönster. En viktig
förutsättning för AI är maskininlärning: en metod där datorer lär sig hantera
uppgifter utan att vara programmerade för den specifika uppgiften. Datorerna lär
sig genom algoritmer som hittar komplexa mönster i stora mängder data. Internetkunskap
pekar också på att dagens AI-verktyg inte är smartare än den data de matats med.
Ett vardagsexempel på AI med kamera är att en mobiltelefon känner igen ett ansikte
genom att avbilda det med kameran. Mitt projekt bygger på samma typ av teknik:
ett program som ska känna igen objekt i bilder från en kamera.

## Objektigenkänning

Objektigenkänning (object detection) är en uppgift som innebär att avgöra var
objekt finns i en bild eller ett videoström och vilken klass de tillhör. Enligt
Ultralytics dokumentation är resultatet av en objektigenkännare en mängd rutor
(bounding boxes) som omsluter objekten i bilden, tillsammans med klassnamn och
konfidensvärden för varje ruta. Objektigenkänning är ett bra val när man vill
veta vilka objekt som finns i en scen, men inte behöver veta objektets exakta form.
Det är precis det mitt program ska göra: för varje bildruta från kameran ska
programmet visa namn, konfidens och rita en ruta runt varje upptäckt objekt.

## YOLO

YOLO är en typ av modell för objektigenkänning som finns i biblioteket
Ultralytics. Enligt Ultralytics dokumentation finns det förtränade modeller
som laddas ner automatiskt vid första användningen. Jag använder en sådan
förtränad modell och tränar ingen egen modell från grunden. Modellerna är
förtränade på COCO-datasetet. Ultralytics beskriver också sina modeller som
optimerade för realtidsinferens, vilket gör dem användbara när bilderna ska
bearbetas snabbt medan kameran körs. YOLO-modellerna finns i olika
storlekar (t.ex. n, s, m, l, x) där de mindre modellerna är snabbare och de
större är mer precisa. Jag använder den lilla modellen `yolov8n.pt` eftersom
den ska hinna med att köra i realtid på min dator.

## Python

Python är det programmeringsspråk jag skriver projektet i. Min källa är
Pythons officiella dokumentation, som jag använder som uppslagsverk när jag
behöver. Jag valde Python eftersom
både OpenCV och Ultralytics har stöd för språket, och eftersom det är språket
jag använder i kursen.

## Kamera och videoström med OpenCV

OpenCV är ett bibliotek för bildbehandling som har stöd för att läsa video från
en kamera. Enligt OpenCV:s dokumentation "Getting Started with Videos" skapar man
ett `VideoCapture`-objekt där argumentet kan vara ett enhetsindex, alltså ett
nummer som anger vilken kamera som ska användas (0 för den första kameran).
Därefter kan man fånga bildruta efter bildruta i en loop med `cap.read()`. Om
bilden läses in korrekt returneras True, annars kan man avsluta loopen. Bilderna
visas med `imshow` och väntar på tangenttryck med `waitKey`. När man är klar
släpper man kameran med `cap.release()`. En videoström är alltså en följd av
enskilda bildrutor som läses in och bearbetas en i taget – det är precis så
mitt program fungerar.

## Realtidsdetektion

Realtidsdetektion betyder att varje bildruta från kameran hinner bearbetas och
visas så fort att bilden upplevs som flytande. Programmet kör en kontinuerlig
loop: läs en bildruta → kör YOLO på rutan → rita ut rutor med namn och konfidens
→ visa bilden → upprepa. Ultralytics skriver att deras modeller är optimerade
för realtidsinferens. Hur fort det faktiskt går beror även på vilken dator man
använder, därför visar mitt program FPS (bilder per sekund) så att jag kan
se om programmet hinner med i realtid.

## Koppling till mitt gymnasiearbete: matsvinn och hållbarhet

Jag har valt att koppla projektet till frågan om matsvinn och hållbarhet.
Naturvårdsverket skriver att livsmedelskonsumtion står för 29 procent av
hushållens konsumtionsbaserade växthusgasutsläpp, och att minskat matsvinn
bland annat innebär ökad resurseffektivitet och minskad miljöbelastning.
Naturvårdsverket anger också att hushållen står för 637 000 ton livsmedelsavfall,
ungefär 60 kg per person och år 2024. Matsvinn uppstår i hela livsmedelskedjan,
bland annat i hushållen.

Objektigenkänning är en grundläggande AI-funktion som gör att en dator kan se
vad som finns i en bild. Genom att bygga ett sådant program lär jag mig hur
tekniken fungerar i praktiken. Jag vill vara tydlig med att mitt program
minskar inte matsvinn i dagens skick – det känner igen enkla objekt som kopp
och flaska. Kopplingen är att tekniken är ett verktyg som bland annat kan
användas i system där man behöver veta vad som finns i en bild, och att jag
genom projektet har lärt mig grunderna i en teknik som används i fler
sammanhang än mitt eget.

## Källor

- Internetkunskap – Artificiell intelligens
  https://internetkunskap.se/artiklar/ordlista/artificiell-intelligens/
- Python official documentation
  https://docs.python.org/sv/3/
- OpenCV official documentation – Getting Started with Videos
  https://docs.opencv.org/5.0.0-alpha/dd/d43/tutorial_py_video_display.html
- Ultralytics official documentation – Object Detection
  https://docs.ultralytics.com/tasks/detect
- Naturvårdsverket – Matsvinn och livsmedelsavfall
  https://www.naturvardsverket.se/amnesomraden/avfall/avfallslag/matsvinn-och-livsmedelsavfall/
