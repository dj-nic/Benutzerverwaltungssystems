BENUTZER_RECHTE = {
    "Benutzer": ["Benutzer"],
    "Lehrer": ["Benutzer", "Lehrer"],
    "Admin": ["Benutzer", "Admin"],
    "Schueler": ["Benutzer", "Schueler"]
}

class Benutzer:
    def __init__(self, name, passwort=None, loginStatus=False, rolle="Benutzer"):
        self.name = name
        self.passwort = passwort
        self.loginStatus = loginStatus
        self.rolle = rolle
        self.rechte = BENUTZER_RECHTE.get(rolle, [])

    def getBenutzername(self):
        return self.name
    
    def getPasswort(self):
        return self.passwort
    
    def getLoginStatus(self):
        return self.loginStatus
    
    def getRechte(self):
        return self.rechte
    

class Lehrer(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Lehrer")

class Admin(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Admin")

class Schueler(Benutzer):
    def __init__(self, name, passwort=None, loginStatus=False):
        super().__init__(name, passwort, loginStatus, rolle="Schueler")

