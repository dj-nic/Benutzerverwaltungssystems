import Benutzer as Benutzer
def main():
    # Erstellen eines Benutzerobjekts
    benutzer = Benutzer.Benutzer
    benutzer1 = benutzer("Max Mustermann", "passwort123")

    print("Benutzername:", benutzer1.getBenutzername())
    print("Passwort:", benutzer1.getPasswort())
    print("Login Status:", benutzer1.getLoginStatus())
    print("Rechte:", benutzer1.getRechte())


if __name__ == "__main__":
    main()