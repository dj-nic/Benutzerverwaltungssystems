import Benutzer as Benutzer

def registrieren():
    print("\n--- Registrierung ---")
    username = input("Neuer Benutzername: ")
    if username in Benutzer.Benutzer.alleBenutzer:
        print("Benutzername existiert bereits!")
        return None
    passwort = input("Passwort: ")
    rolle = input("Rolle (Benutzer/Schueler/Lehrer/Admin): ")
    if rolle not in ["Benutzer", "Schueler", "Lehrer", "Admin"]:
        print("Ungültige Rolle. Standardrolle 'Benutzer' wird verwendet.")
        rolle = "Benutzer"
    neuer_benutzer = Benutzer.getBenutzerKlasse(rolle)(username, passwort)
    print(f"Benutzer '{username}' mit Rolle '{rolle}' wurde registriert.")
    return neuer_benutzer

def login():
    print("\n--- Login ---")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    if username in Benutzer.Benutzer.alleBenutzer and password == Benutzer.Benutzer.alleBenutzer[username].getPasswort():
        print("Login erfolgreich!")
        return Benutzer.Benutzer.alleBenutzer[username]
    elif username not in Benutzer.Benutzer.alleBenutzer:
        print("Benutzername nicht gefunden.")
        return None
    else:
        print("Login fehlgeschlagen. Benutzername oder Passwort falsch.")
        return None

def home_menu(benutzer):
    while True:
        print(f"\n--- Home Menü ({benutzer.rolle}) ---")
        if benutzer.rolle == "Schueler":
            print("1. Benutzerprofil anzeigen")
            print("2. Noten anzeigen")
            print("3. Kurse anzeigen")
            print("4. Abmelden")
            auswahl = input("Bitte wählen (1-4): ")
            if auswahl == "4":
                print("Abgemeldet.")
                break
            else:
                print("Funktion noch nicht implementiert.")
        elif benutzer.rolle == "Lehrer":
            print("1. Benutzerprofil anzeigen")
            print("2. Noten verwalten")
            print("3. Kurse verwalten")
            print("4. Abmelden")
            auswahl = input("Bitte wählen (1-4): ")
            if auswahl == "4":
                print("Abgemeldet.")
                break
            else:
                print("Funktion noch nicht implementiert.")
                
        elif benutzer.rolle == "Admin":
            print("1. Benutzer verwalten")
            print("2. Systemeinstellungen")
            print("3. Abmelden")
            auswahl = input("Bitte wählen (1-3): ")
            if auswahl == "1":
                benutzer.benutzer_verwalten()
            elif auswahl == "2":
                benutzer.systemeinstellungen()
            elif auswahl == "3":
                print("Abgemeldet.")
                break
            else:
                print("Ungültige Auswahl.")

        else:
            print("1. Profil anzeigen")
            print("2. Abmelden")
            auswahl = input("Bitte wählen (1-2): ")
            if auswahl == "2":
                print("Abgemeldet.")
                break
            else:
                print("Funktion noch nicht implementiert.")

def login_menu():
    while True:
        print("\n--- Hauptmenü ---")
        print("1. Einloggen")
        print("2. Registrieren")
        print("3. Beenden")
        auswahl = input("Bitte wählen (1-3): ")
        if auswahl == "1":
            benutzer = login()
            if benutzer:
                print("Willkommen im System!")
                home_menu(benutzer)
        elif auswahl == "2":
            registrieren()
        elif auswahl == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")

def main():
    # Beispielbenutzer für Testzwecke
    benutzer1 = Benutzer.Benutzer("Max Mustermann", "passwort123")
    login_menu()

if __name__ == "__main__":
    main()