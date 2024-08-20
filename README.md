# Realtime Latency Visualiser

Dieses Werkzeug wurde von Felix Kuhlmann im Rahmen des Moduls "Grundkurs Python" bei Professor Odefey programmiert.

## Installation und Programmstart
Die folgenden externen Module werden in diesem Projekt genutzt:

- PySide6
- Numpy

Die Installation aller benötigten Dependenzen erfolgt hier über `requirements.txt`. 
Im Idealfall führt man die Installation in einem *virtual environment* aus, um sein System nicht mit den relativ großen Paketen von PySide6 zu belasten.  
Die Befehle zum Erstellen des *venv* und zum Starten der Installation sind untenstehend aufgeführt.

```bash
python3 -m venv <projektverzeichnis>
source <projektverzeichnis>/bin/activate
cd <projektverzeichnis>
pip3 install -r requirements.txt
```

> Windows-Nutzende können den Schritt mit dem *venv* auch komplett überspringen und direkt die Dependenzen installieren.

Anschließend wird das Programm mit dem folgenden Befehl gestartet:

|Windows|Linux|
|:-------|:-----|
|start.bat|./start.sh|

Falls unter Linux das Programm nicht starten sollte, weil die Datei nicht ausführbar ist, sollte man den entsprechenden Filemode einstellen.
