import sqlite3

def aggiungi_utente(nome, email):
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO utenti (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print("Utente aggiunto!")
    except sqlite3.IntegrityError:
        print("Errore: l'email è già registrata.")
    conn.close()

def visualizza_utenti():
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utenti")
    utenti = cursor.fetchall()
    conn.close()
    if utenti:
        print("Lista utenti:")
        for utente in utenti:
            print(f"ID: {utente[0]}, Nome: {utente[1]}, Email: {utente[2]}")
    else:
        print("Nessun utente registrato.")

def cancella_utente(utente_id):
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM utenti WHERE id = ?", (utente_id,))
    if cursor.rowcount > 0:
        print("Utente eliminato con successo!")
    else:
        print("Utente non trovato.")
    conn.commit()
    conn.close()

def report_utenti():
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM utenti")
    totale = cursor.fetchone()[0]
    conn.close()
    print(f"Totale utenti registrati: {totale}")

