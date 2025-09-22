from pymongo import MongoClient
from datetime import datetime, timezone

client = MongoClient("mongodb://localhost:27017/")
db = client["smart_notes"]
collection = db["notes"]

# collection.delete_many({})

seed_notes = [
    {
        "title": "Was ist ACID?",
        "content": "ACID steht für Atomicity, Consistency, Isolation und Durability. Es soll die Verlässlichkeit und Integrität von Datenbank-Transaktionen sichern.",
        "tags": ["acid", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Atomicity in ACID...",
        "content": "Atomität: Die einzelnen 'Writes' einer Transaktion werden gemeinsam ausgeführt und können nicht in kleinere Teile unterteilt werden. Treten Fehler bei einer Transaktion auf, werden alle 'Writes' zurückgenommen. Atomicity heißt also 'Alles oder nichts'.",
        "tags": ["acid", "datenbank", "atomicity"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Consistency in ACID...",
        "content": "Konsistenz: Tabellenbeschränkungen in ACID-Datenbanken erfordern, dass alle Transaktionen Daten in einem konsistenten Format speichern.",
        "tags": ["acid", "consistency", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Isolation in ACID...",
        "content": "Isolation stellt sicher, dass die Transaktionen keine schmutzigen Lese- oder Schreibvorgänge zurückgeben, indem sie Daten isoliert und Transaktionen nacheinander durchführt.",
        "tags": ["acid", "isolation", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Durability in ACID...",
        "content": "Langlebigkeit: Systemausfälle (z.B. ein Stromausfall) können Transaktionen beeinträchtigen, sodass eine ACID-Datenbank sicherstellt, dass ein Failover Datenverlust durch ein kritisches Ereignis verhindert.",
        "tags": ["acid", "durability", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Arten der NoSQL-Datenbanken",
        "content": "Es gibt verschiedene Arten von NoSQL-Datenbanken, darunter Dokumenten-, Schlüssel-Wert-, Spalten- und Graphdatenbanken, die jeweils für unterschiedliche Anwendungsfälle konzipiert sind. Bekannte Beispiele sind MongoDB (Dokument), Redis (Schlüssel-Wert), Cassandra (Breitspalten-Store) und Neo4j (Graph).",
        "tags": ["nosql", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Dokumentenbasierte Datenbanken",
        "content": "Dokumentendatenbanken speichern Daten in flexiblen, JSON-ähnlichen Dokumenten, was sie ideal für sich schnell ändernde Daten macht. Beispiele sind MongoDB und CouchDB",
        "tags": ["nosql", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Key-Value-Datenbanken",
        "content": "Schlüssel-Wert-Speicher sind die einfachste Form, die Daten als eindeutige Schlüssel mit zugehörigen Werten speichert, und sind für schnelle Lese-/Schreibvorgänge optimiert. Beispiele sind Redis und Aerospike",
        "tags": ["nosql", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Spaltenorientierte Datenbanken",
        "content": "Spaltenorientierte Datenbanken (auch Breitspalten-Stores genannt) organisieren Daten in Spalten statt in Zeilen und eignen sich gut für sehr große Datensätze mit variabler Struktur. Cassandra ist ein bekanntes Beispiel.",
        "tags": ["nosql", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
    {
        "title": "Graphen-Datenbank",
        "content": "Graphdatenbanken sind speziell für Daten ausgelegt, bei denen die Beziehungen zwischen den Datenelementen im Vordergrund stehen. Neo4j ist ein Beispiel für eine Graphdatenbank.",
        "tags": ["nosql", "datenbank"],
        "created_at": datetime.now(timezone.utc),
    },
]

collection.insert_many(seed_notes)

print("Datenbank wurde mit Beispiel-Notizen!")
