@echo off
echo Aktualisiere News-Daten...
python fetch_news.py
if errorlevel 1 (
    echo Fehler beim Aktualisieren der Daten.
    pause
)

echo Starte lokalen Server unter http://localhost:8000
start http://localhost:8000
python -m http.server 8000
