import Benutzer as Benutzer

def registrieren():
    print("\n--- Registrierung ---")
    username = input("Neuer Benutzername: ")
    if username in Benutzer.Benutzer.alleBenutzer:
        print("Benutzername wurde bereitsvergeben")
        return None
    passwort = input("Passwort: ")
    rolle = input("Rolle (Benutzer/Schueler/Lehrer/Admin): ")
    if rolle not in ["Benutzer", "Schueler", "Lehrer", "Admin"]:
        print("Ungültige Rolle.")
        return None
    neuer_benutzer = Benutzer.getBenutzerKlasse(rolle)(username, passwort)
    print(f"Benutzer '{username}' mit Rolle '{rolle}' wurde registriert.")
    return neuer_benutzer

def login():
    print("\n--- Login ---")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    if username in Benutzer.Benutzer.alleBenutzer and password == Benutzer.Benutzer.alleBenutzer[username].getPasswort():
        print("Hat Geklappt")
        Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(True)
    elif username not in Benutzer.Benutzer.alleBenutzer:
        print("Benutzer nicht gefunden.")
        return None
    else:
        print("Benutzername oder Passwort falsch.")
        return None

def home_menu(benutzer):
    while True:
        username = benutzer.getBenutzername()
        print(f"\n--- Home Menü ({benutzer.rolle}) ---")
        if benutzer.rolle == "Schueler":
            print("1. Benutzerprofil anzeigen")
            print("2. Noten anzeigen")
            print("3. Kurse anzeigen")
            print("4. Abmelden")
            auswahl = input("Bitte wählen (1-4): ")
            if auswahl == "1":
                print(f"Profil von {benutzer.getBenutzername()}:")
                benutzer.info()
            elif auswahl == "2":
                print("...")
            elif auswahl == "3":
                print("...")
            elif auswahl == "4":
                print("Abgemeldet.")
                Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(False)
                break
        elif benutzer.rolle == "Lehrer":
            print("1. Benutzerprofil anzeigen")
            print("2. Klassenliste anzeigen")
            print("3. Abmelden")
            auswahl = input("Bitte wählen (1-4): ")
            if auswahl == "1":
                print(f"Profil von {benutzer.getBenutzername()}:")
                benutzer.info()
            elif auswahl == "2":
                return Benutzer.Lehrer.zeige_klassenliste(benutzer)
            elif auswahl == "3":
                print("Abgemeldet.")
                Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(False)
                break
            else:
                print("Funktion noch nicht implementiert.")
                
        elif benutzer.rolle == "Admin":
            print("1. Alle Benutzer anzeigen")
            print("2. Benutzer löschen")
            print("3. Abmelden")
            auswahl = input("Bitte wählen (1-3): ")
            if auswahl == "1":
                benutzer.zeige_alle_benutzer()
            elif auswahl == "2":
                zu_loeschen = input("Benutzernamen zum Löschen eingeben: ")
                benutzer.benutzer_loeschen(zu_loeschen)
            elif auswahl == "3":
                print("Abgemeldet.")
                Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(False)
                break
            else:
                print("Ungültige Auswahl.")

        else:
            print("1. Profil anzeigen")
            print("2. Abmelden")
            auswahl = input("Bitte wählen (1-2): ")
            if auswahl == "1":
                print(f"Profil von {benutzer.getBenutzername()}:")
                benutzer.info()
            elif auswahl == "2":
                print("Abgemeldet.")
                Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(False)
                Benutzer.Benutzer.alleBenutzer[username].getloginStatus()
                break

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
                print("Login erfolgreich")
                home_menu(benutzer)
        elif auswahl == "2":
            registrieren()
        elif auswahl == "3":
            print("Tschüss")
            break
        else:
            print("Ungültige Auswahl.")

def main():
    login_menu()

if __name__ == "__main__":
    main()