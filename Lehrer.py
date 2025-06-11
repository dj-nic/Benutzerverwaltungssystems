from Benutzer import Benutzer

class Lehrer(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False, fach = None, klasse = None):
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
        
    def info(self):
        super().info()
        print(f"Fach: {self.fach if self.fach else 'Nicht zugewiesen'}")
        if self.klasse:
            print(f"Klassen: {', '.join(self.klasse)}")
        else:
            print("Klassen: Keine Klassen zugewiesen.")