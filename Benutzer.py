import abc
BENUTZER_RECHTE = {
    "Benutzer": ["Benutzer"],
    "Lehrer": ["Benutzer", "Lehrer"],
    "Admin": ["Benutzer", "Admin"],
    "Schueler": ["Benutzer", "Schueler"]
}


class Benutzer(abc.ABC):
    anzahl_benutzer = 0  # Klassenattribut für die Gesamtanzahl
    alleBenutzer = {}  # Klassenattribut für alle Benutzer

    def __init__(self, name, passwort=None, loginStatus=False, rolle="Benutzer"):
        self.name = name
        self.passwort = passwort
        self.loginStatus = loginStatus
        self.rolle = rolle
        self.rechte = BENUTZER_RECHTE.get(rolle, [])
        Benutzer.anzahl_benutzer += 1
        Benutzer.alleBenutzer[name] = self

    # Getter-Methoden
    def getBenutzername(self):
        return self.name
    
    def getPasswort(self):
        return self.passwort
    
    def getLoginStatus(self):
        return self.loginStatus
    
    def getRechte(self):
        return self.rechte

    # Setter-Methoden
    def setBenutzername(self, name):
        self.name = name
    
    def setPasswort(self, passwort):
        self.passwort = passwort
    
    def setLoginStatus(self, status):
        self.loginStatus = status
    
    def setRolle(self, rolle):
        self.rolle = rolle
        self.rechte = BENUTZER_RECHTE.get(rolle, [])

    # Klassenmethode
    @classmethod
    def zeige_anzahl_benutzer(cls):
        return cls.anzahl_benutzer
    def info(self):
        print("=== Info ===")
        print(f"Name: {self.name}")
        print(f"Rolle: {self.rolle}")
        print(f"Login-Status: {'Eingeloggt' if self.loginStatus else 'Ausgeloggt'}")
        print(f"Rechte: {', '.join(self.rechte)}")
    

    

class Lehrer(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Lehrer")

class Admin(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Admin")

class Schueler(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Schueler")

def getBenutzerKlasse(rolle):
    if rolle == "Lehrer":
        return Lehrer
    elif rolle == "Admin":
        return Admin
    elif rolle == "Schueler":
        return Schueler
    else:
        return Benutzer

def getBenutzerRechte(rolle):
    return BENUTZER_RECHTE.get(rolle, [])