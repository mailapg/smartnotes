# smartnotes

## Development

### MongoDB
Man benötigt eine lokale Instanz von MongoDB unter localhost mit Port 27017

### Paketmanager 'uv' installieren
Dazu in der Powershell eingeben:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Danach einmal das Terminal neu starten und mit "uv --version" testen.

### Abhängigkeiten installieren
Dazu einfach 'uv sync' eingeben.

### Projekt starten
uv run fastapi dev