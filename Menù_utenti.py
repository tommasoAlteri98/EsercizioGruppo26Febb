
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
