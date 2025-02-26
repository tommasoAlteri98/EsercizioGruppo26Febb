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

def aggiungi_hotel(nome, descrizione):
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hotel (nome, descrizione) VALUES (?, ?)", (nome, descrizione))
    conn.commit()
    conn.close()
    print("Hotel aggiunto con successo!")

def effettua_prenotazione(utente_id, hotel_id, data_prenotazione):
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prenotazioni (utente_id, hotel_id, data_prenotazione) VALUES (?, ?, ?)", (utente_id, hotel_id, data_prenotazione))
    conn.commit()
    conn.close()
    print("Prenotazione effettuata con successo!")

def visualizza_prenotazioni():
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prenotazioni")
    prenotazioni = cursor.fetchall()
    conn.close()
    if prenotazioni:
        print("📋 Lista prenotazioni:")
        for prenotazione in prenotazioni:
            print(f"ID: {prenotazione[0]}, Utente ID: {prenotazione[1]}, Hotel ID: {prenotazione[2]}, Data: {prenotazione[3]}, Stato: {prenotazione[4]}")
    else:
        print("Nessuna prenotazione registrata.")

def cancella_prenotazione(prenotazione_id):
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prenotazioni WHERE id = ?", (prenotazione_id,))
    if cursor.rowcount > 0:
        print("✅ Prenotazione eliminata con successo!")
    else:
        print("Prenotazione non trovata.")
    conn.commit()
    conn.close()

def report_prenotazioni():
    conn = sqlite3.connect("gestionale.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM prenotazioni")
    totale = cursor.fetchone()[0]
    conn.close()
    print(f"Totale prenotazioni registrate: {totale}")

if __name__ == "__main__":
    while True:
        print("\nGestione Prenotazioni")
        print("1. Aggiungi utente")
        print("2. Aggiungi hotel")
        print("3. Effettua prenotazione")
        print("4. Visualizza prenotazioni")
        print("5. Cancella prenotazione")
        print("6. Mostra report prenotazioni")
        print("7. Esci")
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == "1":
            nome = input("Inserisci il nome: ")
            email = input("Inserisci l'email: ")
            aggiungi_utente(nome, email)
        elif scelta == "2":
            nome = input("Inserisci il nome dell'hotel: ")
            descrizione = input("Inserisci la descrizione dell'hotel: ")
            aggiungi_hotel(nome, descrizione)
        elif scelta == "3":
            utente_id = input("Inserisci ID utente: ")
            hotel_id = input("Inserisci ID hotel: ")
            data_prenotazione = input("Inserisci la data (YYYY-MM-DD): ")
            effettua_prenotazione(utente_id, hotel_id, data_prenotazione)
        elif scelta == "4":
            visualizza_prenotazioni()
        elif scelta == "5":
            prenotazione_id = input("Inserisci ID prenotazione da cancellare: ")
            cancella_prenotazione(prenotazione_id)
        elif scelta == "6":
            report_prenotazioni()
        elif scelta == "7":
            break
        else:
            print("Scelta non valida.")
