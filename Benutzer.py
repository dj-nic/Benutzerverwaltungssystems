class Benutzer:
    def __init__(self, name, passwort=None, loginStatus=False):
        self.name = name
        self.passwort = passwort
        self.loginStatus = loginStatus
        self.rechte = []
        self.rechte.append("Benutzer")

    def getBenutzername(self):
        return self.name
    
    def getPasswort(self):
        return self.passwort
    
    def getLoginStatus(self):
        return self.loginStatus
    
    def getRechte(self):
        return self.rechte

    
# Kleinsten Rechte
    