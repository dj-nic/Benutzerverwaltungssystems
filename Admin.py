import Benutzer

class Admin(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Admin")

    def zeige_alle_benutzer(self):
        print("--- Alle Benutzer ---")
        for benutzer in Benutzer.alleBenutzer.values():
            print(f"Name: {benutzer.getBenutzername()}, Rolle: {benutzer.rolle}")

    def benutzer_loeschen(self, benutzername):
        if benutzername in Benutzer.alleBenutzer:
            del Benutzer.alleBenutzer[benutzername]
            print(f"Benutzer '{benutzername}' wurde gelöscht.")
        else:
            print(f"Benutzer '{benutzername}' wurde nicht gefunden.")


