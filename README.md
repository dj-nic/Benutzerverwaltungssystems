<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-FFCA28?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/OOP-Object%20Oriented-blue?style=for-the-badge" alt="OOP">
  <img src="https://img.shields.io/badge/Scrum-Agile-green?style=for-the-badge" alt="Scrum">
</p>

---
# User Stories und zugehörige Tasks (Scrum-Backlog)

## 1. Als Systementwickler möchte ich eine Oberklasse **Benutzer** implementieren, die allgemeine Eigenschaften und Methoden für alle Benutzer bereitstellt.
**Tasks:**
- Eigenschaften und Methoden für die Oberklasse festlegen (z.B. Name, Passwort, Login-Status)
- Klasse `Benutzer` in Code anlegen
- Getter- und Setter-Methoden implementieren
- Dokumentation der Klasse und Methoden schreiben

---

## 2. Als Systementwickler möchte ich Unterklassen **Schueler**, **Lehrer** und **Administrator** definieren, die sich von Benutzer ableiten und jeweils spezifische Funktionen erhalten.
**Tasks:**
- Anforderungen/Spezialfunktionen pro Unterklasse definieren
- Unterklassen `Schueler`, `Lehrer`, `Administrator` im Code anlegen
- Vererbung von `Benutzer` umsetzen
- Spezifische Methoden/Eigenschaften je Unterklasse implementieren
- Tests für die Vererbung und Spezialfunktionen schreiben

---

## 3. Als Entwickler möchte ich eine Methode zum **Ein- und Ausloggen** entwickeln, damit Benutzer simuliert werden können.
**Tasks:**
- Methoden `login()` und `logout()` in der Klasse `Benutzer` implementieren
- Statuswechsel und Rückgaben testen
- Fehlermeldungen bei falschem Login implementieren

---

## 4. Als Administrator möchte ich **Benutzer erstellen, löschen und anzeigen** können, um grundlegende Verwaltungsfunktionen zu ermöglichen.
**Tasks:**
- Methoden zur Benutzererstellung in der Administrator-Klasse implementieren
- Methoden zum Löschen von Benutzern implementieren
- Methode zur Anzeige aller Benutzer implementieren
- Benutzerliste speichern und verwalten

---

## 5. Als Lehrer möchte ich **Klassenlisten einsehen** können, um die Schülerverwaltung zu erleichtern.
**Tasks:**
- Datenstruktur zur Verwaltung von Klassen und Schülern erstellen
- Methode zum Anzeigen der Klassenliste in der `Lehrer`-Klasse implementieren
- Testdaten für Klassen und Schüler anlegen

---

## 6. Als Schüler möchte ich **meine persönlichen Noten einsehen** können, um meine Leistungen zu verfolgen.
**Tasks:**
- Notenverwaltung für Schüler umsetzen
- Methode zum Anzeigen der eigenen Noten in der `Schueler`-Klasse implementieren
- Beispielnoten zu Testzwecken anlegen

---

## 7. Als Entwickler möchte ich ein Klassenattribut **anzahl_benutzer** einsetzen, um die Gesamtanzahl aller erzeugten Benutzer zu zählen.
**Tasks:**
- Attribut `anzahl_benutzer` als Klassenattribut in `Benutzer` implementieren
- Logik zum Hochzählen und ggf. Verringern der Anzahl bei Erstellung/Löschung implementieren

---

## 8. Als Entwickler möchte ich eine Klassenmethode **zeige_anzahl_benutzer()** implementieren, die diese Zahl zurückliefert.
**Tasks:**
- Klassenmethode in `Benutzer` implementieren
- Methode testen

---

## 9. Als Entwickler möchte ich **Konstruktoren in allen Unterklassen korrekt mit `super()` erweitern**, um Wiederverwendbarkeit und Konsistenz zu gewährleisten.
**Tasks:**
- Konstruktoren mit `super()` in `Schueler`, `Lehrer`, `Administrator` implementieren
- Tests zur Initialisierung und Vererbung schreiben

---

## 10. Als Entwicklerteam möchte ich den **Bearbeitungsstatus aller Aufgaben über das Moodle-Kanban-Board dokumentieren**, damit die Lehrkraft jederzeit einen Einblick in den Projektstand erhält.
**Tasks:**
- Alle User Stories und Tasks auf das Kanban-Board übertragen
- Aufgaben laufend in „To Do“, „In Progress“, „Review“, „Done“ verschieben
- Verantwortlichkeiten pro Task klären und dokumentieren

---

## 11. Als Entwicklerteam möchte ich eine **Abschlusspräsentation vorbereiten**, in der Sie das System technisch und aus Anwendersicht vorstellen.
**Tasks:**
- Gliederung der Präsentation erstellen
- Demo-Szenarien aus Anwendersicht zusammenstellen
- Screenshots oder Live-Demo vorbereiten
- Technische Umsetzung und Herausforderungen erläutern

---

## 12. Als Entwicklerteam möchte ich eine **strukturierte README-Datei erstellen**, in der Sie Ihr System dokumentieren und Hinweise zur Ausführung geben.
**Tasks:**
- Aufbau und Format der README planen
- Projektbeschreibung, Installations- und Nutzungshinweise verfassen
- Beispiele für die Anwendung einfügen
- Hinweise zu Anforderungen und Lizenzen ergänzen

---

## 13. Als Projektteam möchte ich mich mit dem **Scrum-Vorgehensmodell vertraut machen**, um Aufgaben sinnvoll in User-Stories und Tasks aufzuteilen und effektiv im Team zusammenzuarbeiten.
**Tasks:**
- Scrum-Prinzipien und -Rollen recherchieren
- Ablauf eines Sprints und Meetings besprechen
- User-Stories und Tasks gemeinsam formulieren und schätzen
- Review- und Retrospektive-Meetings planen