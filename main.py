import Benutzer as Benutzer
import Admin
import Schueler
import Lehrer

def testdaten_anlegen():
    # Admin
    Admin.Admin("admin", "admin123")
    # Lehrer
    Lehrer.Lehrer("lehrer1", "pwlehrer", fach="Mathe", klasse=["10A"])
    # Schüler mit Noten
    s1 = Schueler.Schueler("max", "pwmax", klasse="10A")
    s1.note_hinzufuegen("Mathe", 2)
    s1.note_hinzufuegen("Deutsch", 3)
    s2 = Schueler.Schueler("lisa", "pwLisa", klasse="10A")
    s2.note_hinzufuegen("Mathe", 1)
    # Benutzer ohne Rolle
    Benutzer.Benutzer("gast", "gastpw")

def registrieren():
    print("--- Registrierung ---")
    username = input("Benutzername: ")
    if username in Benutzer.Benutzer.alleBenutzer:
        print("Name vergeben")
        return None
    passwort = input("Passwort: ")
    rolle = input("Rolle (Benutzer/Schueler/Lehrer/Admin): ")
    if rolle not in ["Benutzer", "Schueler", "Lehrer", "Admin"]:
        print("Ungültige Rolle")
        return None
    if rolle == "Admin":
        neuer_benutzer = Admin.Admin(username, passwort)
    elif rolle == "Schueler":
        klasse = input("Klasse: ")
        neuer_benutzer = Schueler.Schueler(username, passwort, klasse=klasse)
    elif rolle == "Lehrer":
        fach = input("Fach: ")
        neuer_benutzer = Lehrer.Lehrer(username, passwort, fach=fach)
    else:
        neuer_benutzer = Benutzer.Benutzer(username, passwort)
    print(f"{username} ({rolle}) registriert.")
    return neuer_benutzer

def login():
    print("--- Login ---")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    if username in Benutzer.Benutzer.alleBenutzer and password == Benutzer.Benutzer.alleBenutzer[username].getPasswort():
        Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(True)
        return Benutzer.Benutzer.alleBenutzer[username]
    elif username not in Benutzer.Benutzer.alleBenutzer:
        print("Nicht gefunden")
        return None
    else:
        print("Falsche Daten")
        return None

def home_menu(benutzer):
    while True:
        print(f"-- Menü ({benutzer.rolle}) --")
        if benutzer.rolle == "Schueler":
            print("1. Profil\n2. Noten\n3. Kurse\n4. Abmelden")
            auswahl = input("")
            if auswahl == "1":
                benutzer.info()
            elif auswahl == "2":
                noten = benutzer.get_noten()
                if noten:
                    for fach, note in noten.items():
                        print(f"{fach}: {note}")
                else:
                    print("Keine Noten")
            elif auswahl == "3":
                klassen = benutzer.get_klasse()
                print(f"Klasse: {klassen if klassen else 'Keine Klasse zugewiesen'}")
            elif auswahl == "4":
                print("Abgemeldet")
                benutzer.setLoginStatus(False)
                break
        elif benutzer.rolle == "Lehrer":
            print("1. Profil\n2. Klassenliste\n3. Schüler zu Klasse\n4. Note vergeben\n5. Abmelden")
            auswahl = input("")
            if auswahl == "1":
                benutzer.info()
            elif auswahl == "2":
                benutzer.zeige_klassenliste()
            elif auswahl == "3":
                schuelername = input("Schülername: ")
                klasse = input("Klasse: ")
                benutzer.schueler_hinzufuegen(schuelername, klasse)
            elif auswahl == "4":
                schuelername = input("Schülername: ")
                fach = input("Fach: ")
                note = input("Note: ")
                benutzer.note_vergeben(schuelername, fach, note)
            elif auswahl == "5":
                print("Abgemeldet")
                benutzer.setLoginStatus(False)
                break
        elif benutzer.rolle == "Admin":
            print("1. Alle Benutzer\n2. Löschen\n3. Abmelden")
            auswahl = input("")
            if auswahl == "1":
                Benutzer.Benutzer.zeige_anzahl_benutzer()
            elif auswahl == "2":
                zu_loeschen = input("Name: ")
                benutzer.benutzer_loeschen(zu_loeschen) 
            elif auswahl == "3":
                print("Abgemeldet")
                benutzer.setLoginStatus(False)
                break
        else:
            print("1. Profil\n2. Abmelden")
            auswahl = input("")
            if auswahl == "1":
                Admin.Admin.zeige_anzahl_benutzer()
            elif auswahl == "2":
                print("Abgemeldet")
                benutzer.setLoginStatus(False)
                break

def login_menu():
    while True:
        print("-- Hauptmenü --")
        print("1. Login\n2. Registrieren\n3. Ende")
        auswahl = input("")
        if auswahl == "1":
            benutzer = login()
            if benutzer:
                home_menu(benutzer)
        elif auswahl == "2":
            registrieren()
        elif auswahl == "3":
            print("Tschüss")
            break

def main():
    testdaten_anlegen()
    login_menu()

if __name__ == "__main__":
    main()