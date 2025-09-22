# Smart Notes

## Setup

### MongoDB
Es wird eine eine lokale Instanz von MongoDB unter localhost mit Port 27017 benötigt.

### Paketmanager 'uv' installieren
Unter Windows reicht es, folgenden Befehl in der Powershell auszuführen:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Danach einmal das Terminal neu starten und 'uv' testen:
```
uv --version
```
Für andere Betriebssysteme und Installationsalternativen, z.B. 'uv' mittels pip zu installieren, geht es [hier zur Installationsanleitung](https://docs.astral.sh/uv/getting-started/installation/).

### Abhängigkeiten installieren
Es reicht, folgenden Befehl Im Terminal auszuführen:
```
uv sync
```

### Datenbank mit Beispiel-Daten füllen (optional)
```
uv run python app/seed.py
```

### Projekt starten
Im Development-Modus:
```
uv run fastapi dev
```

Oder im Production-Modus:
```
uv run fastapi run
```