import Benutzer

class Lehrer(Benutzer.Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False, fach=None, klasse=None):
        super().__init__(name, passwort, loginStatus, rolle="Lehrer")
        self.fach = fach
        self.klasse = klasse if klasse else []

    def get_fach(self):
        return self.fach

    def get_klasse(self):
        return self.klasse

    def klasse_hinzufuegen(self, neueKlasse):
        if neueKlasse not in self.klasse:
            self.klasse.append(neueKlasse)

    def schueler_hinzufuegen(self, schuelername, klasse):
        from Schueler import Schueler
        if schuelername in Benutzer.Benutzer.alleBenutzer and isinstance(Benutzer.Benutzer.alleBenutzer[schuelername], Schueler):
            schueler = Benutzer.Benutzer.alleBenutzer[schuelername]
            schueler.set_klasse(klasse)
            if klasse not in self.klasse:
                self.klasse.append(klasse)
            print(f"{schuelername} wurde der Klasse {klasse} zugewiesen.")
        else:
            print(f"{schuelername} ist kein Schüler.")

    def note_vergeben(self, schuelername, fach, note):
        from Schueler import Schueler
        if schuelername in Benutzer.Benutzer.alleBenutzer and isinstance(Benutzer.Benutzer.alleBenutzer[schuelername], Schueler):
            schueler = Benutzer.Benutzer.alleBenutzer[schuelername]
            schueler.note_hinzufuegen(fach, note)
            print(f"Note {note} in {fach} an {schuelername} vergeben.")
        else:
            print(f"{schuelername} ist kein Schüler.")

    def zeige_klassenliste(self):
        print("--- Klassenliste ---")
        for benutzer in Benutzer.Benutzer.alleBenutzer.values():
            if hasattr(benutzer, "klasse") and benutzer.rolle == "Schueler":
                print(f"{benutzer.getBenutzername()} (Klasse: {benutzer.get_klasse()})")

    def info(self):
        super().info()
        print(f"Fach: {self.fach if self.fach else 'Nicht zugewiesen'}")
        if self.klasse:
            print(f"Klassen: {', '.join(self.klasse)}")
        else:
            print("Klassen: Keine Klassen zugewiesen.")