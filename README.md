Draw AI
---
AI Draw wurde bei Jugendhackt 2023 (jugendhackt.org) in Köln, Deutschland von Fabio, Amir, Becca, Frédéric und Benjamin entwickelt. Es wurde gebaut und gecodet um Leute die keinen Stift halten können, die Möglichkeit zu geben zu malen und Impressionen auszudrücken.

Technologien
---
Verwendet wurde die AI-Umgebung AUTOMATIC1111 (https://github.com/AUTOMATIC1111/stable-diffusion-webui) sowie die Beispiel API aus dem Wiki-Artikel
(https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API).
Um die Sprache aus der Sprach-Eingabe in Text umzuwandeln haben wir das Python Modul speech_recognition verwendet.
Mittels OpenCV werden die generierten Bilder in für einen Plotter verabeitbare Linien umgewandelt. (Code ist noch nicht verfügbar)
Um den Plotter anzusteuern haben wir einen Arduino mit C++ programmiert. Dieser Teil ist allerdings noch nicht fertig und der Code nicht verfügbar.
