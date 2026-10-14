# Testplan

Här är min plan för att testa programmet inför skolrapporten. Resultaten
skriver jag in i `test_results.csv`. Skärmbilder (`s`-knappen) sparar jag
som bevis.

## Test 1: Olika objekt

Jag visar minst fem olika objekt för kameran, ett i taget, på ungefär 1 m
avstånd och i normal belysning:

- [ ] Mobiltelefon (klass: `cell phone`)
- [ ] Person (klass: `person`)
- [ ] Mugge (klass: `cup`)
- [ ] Flaska (klass: `bottle`)
- [ ] Bok (klass: `book`)
- [ ] Laptop (klass: `laptop`)
- [ ] Två objekt samtidigt (t.ex. en flaska och en mugge) för att testa
      att programmet kan hitta flera objekt i samma bild

## Test 2: Olika avstånd

Jag visar samma objekt (muggen) på olika avstånd från kameran och noterar
om det upptäcks och med vilken konfidens:

- [ ] 0,5 m
- [ ] 1 m
- [ ] 2 m
- [ ] 3 m

Förväntan: ju närmare kameran, desto säkrare upptäckt.

## Test 3: Olika belysning

Samma objekt (muggen), ungefär 1 m avstånd:

- [ ] Normalt inomhusljus
- [ ] Svag belysning (lampan avstängd)
- [ ] Svagt ljus med skrivbordslampa riktad mot objektet
- [ ] Direkt solljus mot kameran (utblåsning)

Förväntan: modellen fungerar bäst i normalt och starkt ljus.

## Test 4: Hastighet (realtid)

Programmet visar FPS (bilder per sekund) i vänstra hörnet. Jag noterar
FPS för tre situationer:

- [ ] Tomt rum (inga objekt)
- [ ] Ett objekt synligt
- [ ] Många objekt synliga

**Godkänt:** FPS över ungefär 15, så att bilden känns flytande (realtid).

## Hur jag fyller i resultatfilen

Varje rad i `test_results.csv` är ett testförsök. Jag trycker `r` i programmet
så skrivs en rad automatiskt med tidsstämpel, upptäckt klass och konfidens.
Sedan fyller jag i resten för hand:

- **tidpunkt** – när jag loggade (fylls i automatiskt)
- **objekt** – vad jag visade för kameran
- **upptaekt_klass** – vilken klass YOLO namngav (t.ex. `cup`)
- **upptackt** – ja/nej
- **konfidens** – siffran programmet visade (0–1)
- **avstand_m** – avståndet i meter
- **belysning** – normal/svag/lampa/sol
- **anteckningar** – t.ex. "fel klass", "fladdrade mellan cup och bowl"
