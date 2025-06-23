import tkinter as tk
from tkinter import messagebox
import Benutzer
import Admin
import Schueler
import Lehrer
import pickle

FONT_FAMILY = "Segoe UI"
LABEL_BENUTZERNAME = "Benutzername:"
BUTTON_ZURUECK = "Zurück"

def benutzer_speichern(dateiname="benutzer.pkl"):
    with open(dateiname, "wb") as f:
        pickle.dump(Benutzer.Benutzer.alleBenutzer, f)

def benutzer_laden(dateiname="benutzer.pkl"):
    try:
        with open(dateiname, "rb") as f:
            Benutzer.Benutzer.alleBenutzer = pickle.load(f)
            Benutzer.Benutzer.anzahl_benutzer = len(Benutzer.Benutzer.alleBenutzer)
    except FileNotFoundError:
        pass

class BenutzerGUI:
    def __init__(self, master):
        benutzer_laden()  # Benutzer beim Start laden
        self.master = master
        self.current_user = None  # aktuell eingeloggter Benutzer
        master.title("Benutzerverwaltungssystem")
        self.center_window(700, 600)  # Fenster mittig setzen
        master.configure(bg="#f5f6fa")  # Helles Hintergrund-Theme
        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(padx=30, pady=30, fill='both', expand=True)
        self.show_login()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        benutzer_speichern()  # Benutzer automatisch speichern
        self.master.destroy()

    def center_window(self, width=700, height=600):
        # Bildschirmgröße ermitteln
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def styled_label(self, text, size=12, bold=False, pady=5):
        font = (FONT_FAMILY, size, "bold" if bold else "normal")
        return tk.Label(self.frame, text=text, font=font, bg="#f5f6fa", fg="#222f3e", pady=pady)

    def styled_button(self, text, command, color="#0984e3"):
        return tk.Button(self.frame, text=text, command=command, bg=color, fg="white", font=(FONT_FAMILY, 11, "bold"), relief="flat", activebackground="#74b9ff", activeforeground="#222f3e", padx=8, pady=6, bd=0, cursor="hand2")

    def styled_entry(self, show=None):
        return tk.Entry(self.frame, font=(FONT_FAMILY, 11), show=show, bg="#dfe6e9", fg="#222f3e", relief="flat", insertbackground="#222f3e")

    def show_login(self):
        self.clear_frame()
        self.styled_label("Login", size=18, bold=True, pady=10).pack(pady=10)
        self.styled_label(LABEL_BENUTZERNAME).pack(anchor='w')
        self.username_entry = self.styled_entry()
        self.username_entry.pack(fill='x', pady=2)
        self.styled_label("Passwort:").pack(anchor='w')
        self.password_entry = self.styled_entry(show="*")
        self.password_entry.pack(fill='x', pady=2)
        self.styled_button("Login", self.login).pack(pady=12, fill='x')
        self.styled_button("Registrieren", self.show_register, color="#636e72").pack(fill='x')

    def show_register(self):
        self.clear_frame()
        self.styled_label("Registrierung", size=18, bold=True, pady=10).pack(pady=10)
        self.styled_label(LABEL_BENUTZERNAME).pack(anchor='w')
        self.reg_username = self.styled_entry()
        self.reg_username.pack(fill='x', pady=2)
        self.styled_label("Passwort:").pack(anchor='w')
        self.reg_password = self.styled_entry(show="*")
        self.reg_password.pack(fill='x', pady=2)
        self.styled_label("Rolle:").pack(anchor='w')
        self.reg_role = tk.StringVar()
        rollen = ["Benutzer", "Schueler", "Lehrer", "Admin"]
        self.reg_role.set(rollen[0])
        # Modernes Dropdown-Menü
        option_menu = tk.OptionMenu(self.frame, self.reg_role, *rollen)
        option_menu.config(font=(FONT_FAMILY, 11), bg="#dfe6e9", fg="#222f3e", relief="flat", highlightthickness=0, activebackground="#b2bec3")
        option_menu['menu'].config(font=(FONT_FAMILY, 11), bg="#dfe6e9", fg="#222f3e")
        option_menu.pack(fill='x', pady=2)
        self.extra_label = self.styled_label("")
        self.extra_label.pack(anchor='w')
        self.extra_entry = self.styled_entry()
        self.extra_entry.pack(fill='x', pady=2)
        self.reg_role.trace("w", self.update_extra_field)
        self.styled_button("Registrieren", self.register).pack(pady=12, fill='x')
        self.styled_button(BUTTON_ZURUECK, self.show_login, color="#636e72").pack(fill='x')
        self.update_extra_field()

    def update_extra_field(self, *args):
        rolle = self.reg_role.get()
        if rolle == "Schueler":
            self.extra_label.config(text="Klasse:")
            self.extra_entry.delete(0, tk.END)
            self.extra_entry.pack(fill='x', pady=2)
        elif rolle == "Lehrer":
            self.extra_label.config(text="Fach:")
            self.extra_entry.delete(0, tk.END)
            self.extra_entry.pack(fill='x', pady=2)
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
        self.styled_label(f"Willkommen, {benutzer.name} ({benutzer.rolle})", size=18, bold=True, pady=10).pack(pady=10)
        if benutzer.rolle == "Schueler":
            self.styled_button("Profil", lambda: self.show_profil(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Noten", lambda: self.show_noten(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Kurse", lambda: self.show_klasse(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Abmelden", self.show_login, color="#636e72").pack(fill='x', pady=10)
        elif benutzer.rolle == "Lehrer":
            self.styled_button("Profil", lambda: self.show_profil(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Klassenliste", lambda: self.show_klassenliste(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Schüler zu Klasse hinzufügen", lambda: self.show_schueler_hinzufuegen(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Note vergeben", lambda: self.show_note_vergeben(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Abmelden", self.show_login, color="#636e72").pack(fill='x', pady=10)
        elif benutzer.rolle == "Admin":
            self.styled_button("Alle Benutzer anzeigen", self.show_alle_benutzer).pack(fill='x', pady=2)
            self.styled_button("Benutzer löschen", self.show_benutzer_loeschen).pack(fill='x', pady=2)
            self.styled_button("Anzahl Benutzer anzeigen", self.show_anzahl_benutzer).pack(fill='x', pady=2)
            self.styled_button("Abmelden", self.show_login, color="#636e72").pack(fill='x', pady=10)
        else:
            self.styled_button("Profil", lambda: self.show_profil(benutzer)).pack(fill='x', pady=2)
            self.styled_button("Abmelden", self.show_login, color="#636e72").pack(fill='x', pady=10)

    def show_profil(self, benutzer):
        self.clear_frame()
        info = f"Name: {benutzer.name}\nRolle: {benutzer.rolle}\nLogin-Status: {'Eingeloggt' if benutzer.loginStatus else 'Ausgeloggt'}\nRechte: {', '.join(benutzer.rechte)}"
        self.styled_label("Profil", size=18, bold=True, pady=10).pack(pady=10)
        self.styled_label(info, pady=5).pack(pady=5)
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(benutzer), color="#636e72").pack(pady=10)

    def show_noten(self, benutzer):
        self.clear_frame()
        self.styled_label("Noten", size=18, bold=True, pady=10).pack(pady=10)
        noten = benutzer.get_noten()
        if (noten):
            for fach, note in noten.items():
                self.styled_label(f"{fach}: {note}", pady=2).pack()
        else:
            self.styled_label("Keine Noten vorhanden.", pady=2).pack()
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(benutzer), color="#636e72").pack(pady=10)

    def show_klasse(self, benutzer):
        self.clear_frame()
        self.styled_label("Kurse/Klasse", size=18, bold=True, pady=10).pack(pady=10)
        klasse = benutzer.get_klasse()
        self.styled_label(f"Klasse: {klasse if klasse else 'Keine Klasse zugewiesen'}", pady=2).pack()
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(benutzer), color="#636e72").pack(pady=10)

    def show_klassenliste(self, benutzer):
        self.clear_frame()
        self.styled_label("Klassenliste", size=18, bold=True, pady=10).pack(pady=10)
        found = False
        for b in Benutzer.Benutzer.alleBenutzer.values():
            if hasattr(b, "klasse") and b.rolle == "Schueler":
                self.styled_label(f"{b.getBenutzername()} (Klasse: {b.get_klasse()})", pady=2).pack()
                found = True
        if not found:
            self.styled_label("Keine Schüler gefunden.", pady=2).pack()
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(benutzer), color="#636e72").pack(pady=10)

    def show_alle_benutzer(self):
        self.clear_frame()
        self.styled_label("Alle Benutzer", size=18, bold=True, pady=10).pack(pady=10)
        for b in Benutzer.Benutzer.alleBenutzer.values():
            self.styled_label(f"Name: {b.getBenutzername()}, Rolle: {b.rolle}", pady=2).pack()
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(self.current_user), color="#636e72").pack(pady=10)

    def show_benutzer_loeschen(self):
        self.clear_frame()
        self.styled_label("Benutzer löschen", size=18, bold=True, pady=10).pack(pady=10)
        self.styled_label(LABEL_BENUTZERNAME).pack(anchor='w')
        self.loesch_entry = self.styled_entry()
        self.loesch_entry.pack(fill='x', pady=2)
        self.styled_button("Löschen", self.benutzer_loeschen, color="#d63031").pack(pady=12, fill='x')
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(self.current_user), color="#636e72").pack(fill='x', pady=10)

    def benutzer_loeschen(self):
        benutzername = self.loesch_entry.get()
        if benutzername in Benutzer.Benutzer.alleBenutzer:
            del Benutzer.Benutzer.alleBenutzer[benutzername]
            messagebox.showinfo("Erfolg", f"Benutzer '{benutzername}' wurde gelöscht.")
        else:
            messagebox.showerror("Fehler", f"Benutzer '{benutzername}' wurde nicht gefunden.")
        self.show_alle_benutzer()

    def show_schueler_hinzufuegen(self, benutzer):
        self.clear_frame()
        self.styled_label("Schüler zu Klasse hinzufügen", size=18, bold=True, pady=10).pack(pady=10)
        self.styled_label("Schülername:").pack(anchor='w')
        self.schuelername_entry = self.styled_entry()
        self.schuelername_entry.pack(fill='x', pady=2)
        self.styled_label("Klasse:").pack(anchor='w')
        self.klasse_entry = self.styled_entry()
        self.klasse_entry.pack(fill='x', pady=2)
        self.styled_button("Hinzufügen", lambda: self.schueler_hinzufuegen_action(benutzer)).pack(pady=12, fill='x')
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(benutzer), color="#636e72").pack(fill='x', pady=10)

    def schueler_hinzufuegen_action(self, benutzer):
        schuelername = self.schuelername_entry.get()
        klasse = self.klasse_entry.get()
        if schuelername in Benutzer.Benutzer.alleBenutzer:
            benutzer.schueler_hinzufuegen(schuelername, klasse)
            messagebox.showinfo("Erfolg", f"{schuelername} wurde der Klasse {klasse} hinzugefügt.")
        else:
            messagebox.showerror("Fehler", f"Schüler '{schuelername}' nicht gefunden.")
        self.show_home(benutzer)

    def show_note_vergeben(self, benutzer):
        self.clear_frame()
        self.styled_label("Note vergeben", size=18, bold=True, pady=10).pack(pady=10)
        self.styled_label("Schülername:").pack(anchor='w')
        self.note_schueler_entry = self.styled_entry()
        self.note_schueler_entry.pack(fill='x', pady=2)
        self.styled_label("Fach:").pack(anchor='w')
        self.note_fach_entry = self.styled_entry()
        self.note_fach_entry.pack(fill='x', pady=2)
        self.styled_label("Note:").pack(anchor='w')
        self.note_note_entry = self.styled_entry()
        self.note_note_entry.pack(fill='x', pady=2)
        self.styled_button("Vergeben", lambda: self.note_vergeben_action(benutzer)).pack(pady=12, fill='x')
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(benutzer), color="#636e72").pack(fill='x', pady=10)

    def note_vergeben_action(self, benutzer):
        schuelername = self.note_schueler_entry.get()
        fach = self.note_fach_entry.get()
        note = self.note_note_entry.get()
        if schuelername in Benutzer.Benutzer.alleBenutzer:
            benutzer.note_vergeben(schuelername, fach, note)
            messagebox.showinfo("Erfolg", f"Note {note} in {fach} an {schuelername} vergeben.")
        else:
            messagebox.showerror("Fehler", f"Schüler '{schuelername}' nicht gefunden.")
        self.show_home(benutzer)

    def show_anzahl_benutzer(self):
        self.clear_frame()
        self.styled_label("Anzahl Benutzer", size=18, bold=True, pady=10).pack(pady=10)
        anzahl = len(Benutzer.Benutzer.alleBenutzer)
        self.styled_label(f"Es gibt aktuell {anzahl} Benutzer.", pady=5).pack(pady=5)
        self.styled_button(BUTTON_ZURUECK, lambda: self.show_home(self.current_user), color="#636e72").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BenutzerGUI(root)
    root.mainloop()
