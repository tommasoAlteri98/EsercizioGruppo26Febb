import sqlite3

conn = sqlite3.connect("gestionale.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS hotel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descrizione TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS prenotazioni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utente_id INTEGER,
    hotel_id INTEGER,
    data_prenotazione TEXT NOT NULL,
    stato TEXT DEFAULT 'attiva',
    FOREIGN KEY (utente_id) REFERENCES utenti(id),
    FOREIGN KEY (hotel_id) REFERENCES hotel(id)
)
""")
conn.commit()

def aggiungi_utente(nome, email):
    cursor.execute("INSERT INTO utenti (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    print("✅ Utente aggiunto!")

def mostra_utenti():
    cursor.execute("SELECT * FROM utenti")
    for utente in cursor.fetchall():
        print(utente)

aggiungi_utente("Mario Rossi", "mario.rossi@email.com")
mostra_utenti()


cursor.close()
conn.close()