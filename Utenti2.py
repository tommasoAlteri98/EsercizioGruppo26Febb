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

if __name__ == "__main__":
    while True:
        print("\nGestione Utenti")
        print("1. Aggiungi utente")
        print("2. Visualizza utenti")
        print("3. Cancella utente")
        print("4. Mostra report utenti")
        print("5. Esci")
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == "1":
            nome = input("Inserisci il nome: ")
            email = input("Inserisci l'email: ")
            aggiungi_utente(nome, email)
        elif scelta == "2":
            visualizza_utenti()
        elif scelta == "3":
            utente_id = input("Inserisci ID utente da cancellare: ")
            cancella_utente(utente_id)
        elif scelta == "4":
            report_utenti()
        elif scelta == "5":
            break
        else:
            print("Scelta non valida.")
