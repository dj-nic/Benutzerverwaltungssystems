import Benutzer

class Schueler(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False, klasse=None):
        super().__init__(name, passwort, loginStatus, rolle="Schueler")
        self.klasse = klasse
        self.noten = {}

    def get_klasse(self):
        return self.klasse

    def get_noten(self):
        return self.noten

    def set_klasse(self, neue_klasse):
        self.klasse = neue_klasse

    def note_hinzufuegen(self, fach, note):
        self.noten[fach] = note

    def info(self):
        print(f"Name: {self.name}, Klasse: {self.klasse}")