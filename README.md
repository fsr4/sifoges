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

### Docker Image
Das Docker Image (OCI) kann einfach mit diesem einen Befehl ausgeführt werden:
```shell
docker run --rm -v <path to working dir>:/app/data ghcr.io/fsr4/sifoges <input filename>
```
`<path to working dir>` ist dabei der Pfad zu dem Ordner, in dem die Input-Datei liegt und in dem die generierte 
PDF-Datei abgespeichert werden soll. `<input filename>` gibt den Namen der Input-Datei im Ordner an.

### "Build from source"
Falls man eine Abneigung gegen OCIs hat, kann man natürlich auch alle Dependencies selbst installieren und das Skript 
so ausführen. Hier der grobe Prozess dafür:

#### Dependencies
* Python 3
* Lokale LaTeX-Installation mit XeTeX
* HTWBerlin Office Schriftart

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

## Font Copyright
Die in diesem Repository enthaltene Schrift "HTWBerlin" wurde von Jürgen Huber und Malte Herok entwickelt und steht 
unter der Lizenz [CC-BY-NC-ND-4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode) für hochschulinterne 
und hochschulöffentliche Zwecke zur Verfügung. Die Nutzung außerhalb des in der 
[EULA](https://corporatedesign.htw-berlin.de/schrift-farbe/schriften/eula/) genannten Umfangs ist nicht gestattet.
