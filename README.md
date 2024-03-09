# AI_Draw
AI Draw wurde bei Jugendhackt 2023 (jugendhackt.org) in Köln, Deutschland von Fabio, Amir, Becca, Frédéric und Benjamin entwickelt. Es wurde gebaut und gecodet um Leute die keinen Stift halten können, die Möglichkeit zu geben zu malen und Impressionen auszudrücken.

## Technologien
Verwendet wurde die AI-Umgebung AUTOMATIC1111 (https://github.com/AUTOMATIC1111/stable-diffusion-webui) sowie die Beispiel API aus dem Wiki-Artikel
(https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API).
Um die Sprache aus der Sprach-Eingabe in Text umzuwandeln haben wir das Python Modul speech_recognition verwendet.
Mittels OpenCV werden die generierten Bilder in für einen Plotter verabeitbare Linien umgewandelt. (Code ist noch nicht verfügbar)
Um den Plotter anzusteuern haben wir einen Arduino mit C++ programmiert. Dieser Teil ist allerdings noch nicht fertig und der Code nicht verfügbar.

## Setup
Um die KI verwenden zu können muss AUTOMATIC1111 installiert und eingerichtet werden.

Dann mit `git clone placeholder` das main.py Skript in einen gewünschten Ordner klonen.
Nun wird mit dem Befehl `python -m venv venvXY` im gleichen Ordner eine virtuelle Umgebung eingerichtet. Hierbei kann venvXY mit einem beliebigen Namen (z.B. ai_venv) ausgetauscht werden. Um die virtuelle Umgebung zu starten muss auf Linux der Befehl `source venvXY/bin/activate` ausgeführt werden. Für Windows siehe hier: https://python.land/virtual-environments/virtualenv
Jetzt können mit den folgenden Befehlen die Abhängigkeiten installiert werden:
```
pip install pip --upgrade  #Um das Tool zum installieren zu aktualisieren.
pip install requests
pip install pillow
pip install SpeechRecognition
pip install sounddevice
pip install pydub
pip install json
pip install base64
pip install io
pip install pyaudio  #Diese Befehele müssen Nacheinander ausgeführt werden.
```
Jetzt kann die KI gestartet werden. Dazu die Anweisungen auf der Seite von AUTOMATIC1111 befolgen.
Dann kann das Programm mit dem folgenden Befehl gestartet werden: `python main.py`

## Nutzung
Wenn das Programm gestartet ist, sollte im Terminal der Text `Recording...` erscheinen. Nun hat man Zeit, der KI einen Prompt zu geben, was sie generieren soll. Dann beginnt die KI ein Bild zu generieren. Dies kann je nach Hardware eine gewisse Zeit dauern. Das Programm ist fertig, wenn in der Konsole der Eingabe-Prompt erscheint. Nun sollte im gleichen Ordner das generierte Bild erscheinen. Das Bild wird nach den Ergebnissen der Spracheingabe benannt.

## Troubleshooting
### main.py wurde nicht gefunden
Sollte die Datei `main.py` nicht gefunden werden, sollte man prüfen, ob man sich im gleichen Ordner befindet. Alternativ kann man das Skript auch durch eine IDE/Entwicklungsumgebung starten.
### Paket XY wurde nicht gefunden
Sollte eine der Abhängigkeiten nicht gefunden werden, kann das mehrere Ursachen haben:
#### Möglichkeit 1: Das installieren der Pakete war nicht erfolgreich.
Das kann man prüfen, indem man die Installation erneut durchführt und auf eventuelle Fehlermeldungen achtet.
#### Möglichkeit 2: Venv
Es kann außerdem vorkommen, dass die Pakete nicht in der Venv installiert wurden. Stellen sie sicher, dass die Venv zum Zeitpunkt der Installation aktiv wahr. Um zu prüfen, dass die Pakete in der Venv sind, kann man außerdem in der Ordnerstruktur der Venv nachsehen. Diese sollten im Ordner `venvXY/lib/pythonXY/site-packages/` zu finden sein.
### Fehler bei der Spracheingabe
Es kann sein, dass nachdem der Text `Recording...` angezeigt wurde ein Fehler auftritt. Dies kann daran liegen, dass kein Audio aufgenommen wurde oder das Mikrofon stummgeschaltet ist.

Falls keiner dieser Fälle eintritt, ist es kein Problem eine neue Issue zu eröffnen. Wir versuchen möglichst schnell darauf zu antworten.
