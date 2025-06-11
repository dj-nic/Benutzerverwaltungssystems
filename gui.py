import tkinter as tk
from tkinter import messagebox
import Benutzer
import Admin
import Schueler
import Lehrer

class BenutzerGUI:
    def __init__(self, master):
        self.master = master
        self.current_user = None  # aktuell eingeloggter Benutzer
        master.title("Benutzerverwaltungssystem")
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        self.show_login()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_frame()
        tk.Label(self.frame, text="Login", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.frame, text="Benutzername:").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()
        tk.Label(self.frame, text="Passwort:").pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()
        tk.Button(self.frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.frame, text="Registrieren", command=self.show_register).pack()

    def show_register(self):
        self.clear_frame()
        tk.Label(self.frame, text="Registrierung", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.frame, text="Benutzername:").pack()
        self.reg_username = tk.Entry(self.frame)
        self.reg_username.pack()
        tk.Label(self.frame, text="Passwort:").pack()
        self.reg_password = tk.Entry(self.frame, show="*")
        self.reg_password.pack()
        tk.Label(self.frame, text="Rolle:").pack()
        self.reg_role = tk.StringVar()
        rollen = ["Benutzer", "Schueler", "Lehrer", "Admin"]
        self.reg_role.set(rollen[0])
        tk.OptionMenu(self.frame, self.reg_role, *rollen).pack()
        self.extra_label = tk.Label(self.frame)
        self.extra_label.pack()
        self.extra_entry = tk.Entry(self.frame)
        self.extra_entry.pack()
        self.reg_role.trace("w", self.update_extra_field)
        tk.Button(self.frame, text="Registrieren", command=self.register).pack(pady=5)
        tk.Button(self.frame, text="Zurück", command=self.show_login).pack()
        self.update_extra_field()

    def update_extra_field(self, *args):
        rolle = self.reg_role.get()
        if rolle == "Schueler":
            self.extra_label.config(text="Klasse:")
            self.extra_entry.delete(0, tk.END)
            self.extra_entry.pack()
        elif rolle == "Lehrer":
            self.extra_label.config(text="Fach:")
            self.extra_entry.delete(0, tk.END)
            self.extra_entry.pack()
        else:
            self.extra_label.config(text="")
            self.extra_entry.delete(0, tk.END)
            self.extra_entry.pack_forget()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in Benutzer.Benutzer.alleBenutzer and password == Benutzer.Benutzer.alleBenutzer[username].getPasswort():
            Benutzer.Benutzer.alleBenutzer[username].setLoginStatus(True)
            self.current_user = Benutzer.Benutzer.alleBenutzer[username]
            self.show_home(self.current_user)
        else:
            messagebox.showerror("Fehler", "Login fehlgeschlagen!")

    def register(self):
        username = self.reg_username.get()
        password = self.reg_password.get()
        rolle = self.reg_role.get()
        if username in Benutzer.Benutzer.alleBenutzer:
            messagebox.showerror("Fehler", "Benutzername vergeben!")
            return
        if rolle == "Admin":
            Admin.Admin(username, password)
        elif rolle == "Schueler":
            klasse = self.extra_entry.get()
            Schueler.Schueler(username, password, klasse=klasse)
        elif rolle == "Lehrer":
            fach = self.extra_entry.get()
            Lehrer.Lehrer(username, password, fach=fach)
        else:
            Benutzer.Benutzer(username, password)
        messagebox.showinfo("Erfolg", f"{username} ({rolle}) registriert.")
        self.show_login()

    def show_home(self, benutzer):
        self.current_user = benutzer
        self.clear_frame()
        tk.Label(self.frame, text=f"Willkommen, {benutzer.name} ({benutzer.rolle})", font=("Arial", 14)).pack(pady=5)
        if benutzer.rolle == "Schueler":
            tk.Button(self.frame, text="Profil", command=lambda: self.show_profil(benutzer)).pack(fill='x')
            tk.Button(self.frame, text="Noten", command=lambda: self.show_noten(benutzer)).pack(fill='x')
            tk.Button(self.frame, text="Kurse", command=lambda: self.show_klasse(benutzer)).pack(fill='x')
            tk.Button(self.frame, text="Abmelden", command=self.show_login).pack(fill='x', pady=10)
        elif benutzer.rolle == "Lehrer":
            tk.Button(self.frame, text="Profil", command=lambda: self.show_profil(benutzer)).pack(fill='x')
            tk.Button(self.frame, text="Klassenliste", command=lambda: self.show_klassenliste(benutzer)).pack(fill='x')
            tk.Button(self.frame, text="Abmelden", command=self.show_login).pack(fill='x', pady=10)
        elif benutzer.rolle == "Admin":
            tk.Button(self.frame, text="Alle Benutzer anzeigen", command=self.show_alle_benutzer).pack(fill='x')
            tk.Button(self.frame, text="Benutzer löschen", command=self.show_benutzer_loeschen).pack(fill='x')
            tk.Button(self.frame, text="Abmelden", command=self.show_login).pack(fill='x', pady=10)
        else:
            tk.Button(self.frame, text="Profil", command=lambda: self.show_profil(benutzer)).pack(fill='x')
            tk.Button(self.frame, text="Abmelden", command=self.show_login).pack(fill='x', pady=10)

    def show_profil(self, benutzer):
        self.clear_frame()
        info = f"Name: {benutzer.name}\nRolle: {benutzer.rolle}\nLogin-Status: {'Eingeloggt' if benutzer.loginStatus else 'Ausgeloggt'}\nRechte: {', '.join(benutzer.rechte)}"
        tk.Label(self.frame, text="Profil", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.frame, text=info, justify='left').pack(pady=5)
        tk.Button(self.frame, text="Zurück", command=lambda: self.show_home(benutzer)).pack(pady=10)

    def show_noten(self, benutzer):
        self.clear_frame()
        tk.Label(self.frame, text="Noten", font=("Arial", 14)).pack(pady=5)
        noten = benutzer.get_noten()
        if (noten):
            for fach, note in noten.items():
                tk.Label(self.frame, text=f"{fach}: {note}").pack()
        else:
            tk.Label(self.frame, text="Keine Noten vorhanden.").pack()
        tk.Button(self.frame, text="Zurück", command=lambda: self.show_home(benutzer)).pack(pady=10)

    def show_klasse(self, benutzer):
        self.clear_frame()
        tk.Label(self.frame, text="Kurse/Klasse", font=("Arial", 14)).pack(pady=5)
        klasse = benutzer.get_klasse()
        tk.Label(self.frame, text=f"Klasse: {klasse if klasse else 'Keine Klasse zugewiesen'}").pack()
        tk.Button(self.frame, text="Zurück", command=lambda: self.show_home(benutzer)).pack(pady=10)

    def show_klassenliste(self, benutzer):
        self.clear_frame()
        tk.Label(self.frame, text="Klassenliste", font=("Arial", 14)).pack(pady=5)
        found = False
        for b in Benutzer.Benutzer.alleBenutzer.values():
            if hasattr(b, "klasse") and b.rolle == "Schueler":
                tk.Label(self.frame, text=f"{b.getBenutzername()} (Klasse: {b.get_klasse()})").pack()
                found = True
        if not found:
            tk.Label(self.frame, text="Keine Schüler gefunden.").pack()
        tk.Button(self.frame, text="Zurück", command=lambda: self.show_home(benutzer)).pack(pady=10)

    def show_alle_benutzer(self):
        self.clear_frame()
        tk.Label(self.frame, text="Alle Benutzer", font=("Arial", 14)).pack(pady=5)
        for b in Benutzer.Benutzer.alleBenutzer.values():
            tk.Label(self.frame, text=f"Name: {b.getBenutzername()}, Rolle: {b.rolle}").pack()
        tk.Button(self.frame, text="Zurück", command=lambda: self.show_home(self.current_user)).pack(pady=10)

    def show_benutzer_loeschen(self):
        self.clear_frame()
        tk.Label(self.frame, text="Benutzer löschen", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.frame, text="Benutzername:").pack()
        self.loesch_entry = tk.Entry(self.frame)
        self.loesch_entry.pack()
        tk.Button(self.frame, text="Löschen", command=self.benutzer_loeschen).pack(pady=5)
        tk.Button(self.frame, text="Zurück", command=lambda: self.show_home(self.current_user)).pack(pady=10)

    def benutzer_loeschen(self):
        benutzername = self.loesch_entry.get()
        if benutzername in Benutzer.Benutzer.alleBenutzer:
            del Benutzer.Benutzer.alleBenutzer[benutzername]
            messagebox.showinfo("Erfolg", f"Benutzer '{benutzername}' wurde gelöscht.")
        else:
            messagebox.showerror("Fehler", f"Benutzer '{benutzername}' wurde nicht gefunden.")
        self.show_alle_benutzer()

if __name__ == "__main__":
    root = tk.Tk()
    app = BenutzerGUI(root)
    root.mainloop()
