# SiFoGeS

Das FSR4-**Si**tzungs**fo**lien**ge**nerator**s**kript dient dazu, basierend auf einer Liste an 
Tagesordnungspunkten eine Präsentation für den FSR4-Moodle-Sitzungsraum zu generieren.

Eine TOP-Datei, die dabei als Input dient, könnte beispielsweise so aussehen:

```
Begrüßung
Feststellung der Beschlussfähigkeit
Beschluss der Tagesordnung
Bestätigung der Protokolle
Inforunde
	Campus Dialog
	Dekanatsfrühstück
	Bericht StuPa
#	Bericht FBR4
Finanzen
Projekte
	Traumwerkstatt
	Rhetorikkurs
Termine
	Nächste Sitzung
	Sonstige Termine
Sonstiges
```

Zeilen, die mit einer Raute `#` starten, gelten dabei als auskommentiert. Alle TOPs, die am Anfang ihrer Zeile 
Whitespace haben, werden als Sub-TOPs dem ersten zuvorigen TOP angehängt, der direkt am Anfang der Zeile steht. 
Verschachtelungen über die zweite Ebene hinaus werden aktuell nicht unterstützt.

## Usage

Um das Tool nutzen zu können, muss erst eine Python-Environment eingerichtet werden. Um alle nötigen Packages in 
einer lokalen Environment zu installieren, können folgende Befehle im Projektordner ausgeführt werden:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Eventuell müssen für die auszuführenden Skripte noch die Permissions richtig gesetzt werden:
```shell
chmod +x generate-slides.sh generate-tex.py
```

Anschließend kann dann eine Präsentation aus einer TOP-Datei generiert werden:
```shell
./generate-slides.sh <top-file>
```

Die resultierende PDF-Datei wird unter dem Namen `main.pdf` im Projektordner gespeichert.

*Note: Die Skripte generieren ein paar temporäre Dateien in einem Unterordner namens `.tmp-xetex`. 
Dieser wird nach erfolgreichem Abschluss des Skripts automatisch gelöscht.*
