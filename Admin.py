from Benutzer import Benutzer, getBenutzerKlasse

class Admin(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Admin")

    def benutzer_verwalten(self):
        while True:
            print("\n--- Benutzerverwaltung ---")
            print("1. Alle Benutzer anzeigen")
            print("2. Neuen Benutzer erstellen")
            print("3. Benutzer löschen")
            print("4. Zurück")
            auswahl = input("Auswahl (1-4): ")

            if auswahl == "1":
                self.zeige_alle_benutzer()
            elif auswahl == "2":
                self.neuen_benutzer_erstellen()
            elif auswahl == "3":
                self.benutzer_loeschen()
            elif auswahl == "4":
                break
            else:
                print("Ungültige Auswahl.")

    def zeige_alle_benutzer(self):
        if not Benutzer.alleBenutzer:
            print("Keine Benutzer vorhanden.")
        else:
            print("\nListe aller Benutzer:")
            for name, benutzer in Benutzer.alleBenutzer.items():
                print(f"- {name} ({benutzer.rolle})")

    def neuen_benutzer_erstellen(self):
        print("\n--- Neuen Benutzer erstellen ---")
        name = input("Benutzername: ")
        if name in Benutzer.alleBenutzer:
            print("Benutzername existiert bereits!")
            return
        passwort = input("Passwort: ")
        rolle = input("Rolle (Benutzer/Schueler/Lehrer/Admin): ")
        if rolle not in ["Benutzer", "Schueler", "Lehrer", "Admin"]:
            print("Ungültige Rolle. 'Benutzer' wird als Standard gesetzt.")
            rolle = "Benutzer"
        klasse = getBenutzerKlasse(rolle)
        klasse(name, passwort)
        print(f"Benutzer '{name}' mit Rolle '{rolle}' wurde erfolgreich erstellt.")

    def benutzer_loeschen(self):
        print("\n--- Benutzer löschen ---")
        name = input("Benutzername zum Löschen: ")
        if name in Benutzer.alleBenutzer:
            del Benutzer.alleBenutzer[name]
            print(f"Benutzer mit Name '{name}' wurde gelöscht.")
        else:
            print("Benutzer nicht gefunden.")
