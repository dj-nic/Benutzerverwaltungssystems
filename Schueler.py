from Benutzer import Benutzer

class Schueler(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False, klasse=None):
        super().__init__(name, passwort, loginStatus, rolle="Schueler")
        self.klasse = klasse
        self.noten = {}
    
    #Methoden
    def get_klasse(self):
        return self.klasse
    
    def get_noten(self):
        return self.noten

    # Setter / Hinzufügen
    def set_klasse(self, neue_klasse):
        self.klasse = neue_klasse

    def note_hinzufuegen(self, fach, note):
        self.noten[fach] = note

    # Info überschreiben
    def info(self):
        super().info()
        print(f"Klasse: {self.klasse}")
        if self.noten:
            print("Noten:")
            for fach, note in self.noten.items():
                print(f"  {fach}: {note}")
        else:
            print("Noch keine Noten vorhanden.")