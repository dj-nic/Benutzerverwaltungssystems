# Zum Hauptinhalt

## Abschlussbedingungen

🧩 **Projektauftrag:** Entwicklung eines rollenbasierten Benutzerverwaltungssystems

🧠 **Handlungssituation**
Die Schulleitung plant die Einführung eines webbasierten Schulportals. Darin sollen verschiedene Benutzergruppen – wie Schüler, Lehrkräfte und Administratoren – unterschiedliche Funktionen und Zugriffsrechte erhalten. Ein externes Entwicklerteam hat mit der Grundentwicklung begonnen, doch die Implementierung eines intelligenten Benutzerrollensystems steht noch aus.

Ihre Aufgabe als Entwicklerteam ist es, diesen Bestandteil zu realisieren. Dabei sollen Sie moderne Prinzipien der objektorientierten Programmierung (OOP) anwenden – insbesondere die Konzepte Vererbung, Klassenattribute und Klassenmethoden.

## 📋 Projektstruktur
Sie arbeiten in Teams von 3–4 Personen über mehrere Unterrichtsstunden hinweg. Ziel ist es, ein funktionsfähiges Python-Modul zu entwickeln, das unterschiedliche Benutzerrollen modelliert. Ihre Arbeitsweise orientiert sich am agilen Scrum-Modell. Am Projektende stellen Sie Ihr Ergebnis im Rahmen einer Kundenpräsentation vor.

## 📌 Ihre Arbeitsaufgaben
- Zerlegen Sie die unten aufgeführten User-Stories in konkrete Tasks.
- Nutzen Sie das von der Lehrkraft in Moodle bereitgestellte Kanban-Board, um Aufgaben fortlaufend zu dokumentieren und den Bearbeitungsstatus zu pflegen.
- Jede Person im Team sollte sichtbar zum Projekterfolg beitragen.
- Am Ende führen Sie eine Kundenpräsentation durch, in der Sie Ihr System technisch und konzeptionell vorstellen.

## 🧭 Einführung in Scrum
Bevor Sie mit der konkreten Entwicklung beginnen, setzen Sie sich mit dem Scrum-Vorgehensmodell auseinander. Ziel ist es, die agile Denkweise zu verstehen und die Arbeitsweise auf das Projekt zu übertragen.

- Was sind User-Stories und wie werden sie formuliert?
- Wie unterscheiden sich User-Stories und Tasks?
- Was ist ein Kanban-Board und wie wird es genutzt?
- Welche Rolle spielt die Teamorganisation im Scrum-Kontext?

## 🧾 User-Stories (Scrum-Backlog)
Formulieren Sie zu jeder User-Story konkrete Aufgaben (Tasks), die Sie auf dem Kanban-Board abbilden.

1. Als Systementwickler möchten Sie eine Oberklasse Benutzer implementieren, die allgemeine Eigenschaften und Methoden für alle Benutzer bereitstellt.
2. Als Systementwickler möchten Sie Unterklassen Schueler, Lehrer und Administrator definieren, die sich von Benutzer ableiten und jeweils spezifische Funktionen erhalten.
3. Als Entwickler möchten Sie eine Methode zum Ein- und Ausloggen entwickeln, damit Benutzer simuliert werden können.
4. Als Administrator möchten Sie Benutzer erstellen, löschen und anzeigen können, um grundlegende Verwaltungsfunktionen zu ermöglichen.
5. Als Lehrer möchten Sie Klassenlisten einsehen können, um die Schülerverwaltung zu erleichtern.
6. Als Schüler möchten Sie Ihre persönlichen Noten einsehen können, um Ihre Leistungen zu verfolgen.
7. Als Entwickler möchten Sie ein Klassenattribut anzahl_benutzer einsetzen, um die Gesamtanzahl aller erzeugten Benutzer zu zählen.
8. Als Entwickler möchten Sie eine Klassenmethode zeige_anzahl_benutzer() implementieren, die diese Zahl zurückliefert.
9. Als Entwickler möchten Sie Konstruktoren in allen Unterklassen korrekt mit super() erweitern, um Wiederverwendbarkeit und Konsistenz zu gewährleisten.
10. Als Entwicklerteam möchten Sie den Bearbeitungsstatus aller Aufgaben über das Moodle-Kanban-Board dokumentieren, damit die Lehrkraft jederzeit einen Einblick in den Projektstand erhält.
11. Als Entwicklerteam möchten Sie eine Abschlusspräsentation vorbereiten, in der Sie das System technisch und aus Anwendersicht vorstellen.
12. Als Entwicklerteam möchten Sie eine strukturierte README-Datei erstellen, in der Sie Ihr System dokumentieren und Hinweise zur Ausführung geben.
13. Als Projektteam möchten Sie sich mit dem Scrum-Vorgehensmodell vertraut machen, um Aufgaben sinnvoll in User-Stories und Tasks aufzuteilen und effektiv im Team zusammenzuarbeiten.

## 🛠️ Technische Hinweise
- Programmiersprache: Python
- Verwenden Sie:
  - Vererbung (`class Unterklasse(Oberklasse):`)
  - Konstruktorverkettung mit `super().__init__()`
  - Klassenattribute (z. B. `anzahl_benutzer = 0`)
- Erstellen Sie ein UML-Klassendiagramm, um die Klassenstruktur und die Vererbungshierarchie Ihres Systems visuell darzustellen.
- Achten Sie auf eine strukturierte Codegestaltung (Kommentare, Methodenaufteilung, saubere Namensgebung)

## 🎓 Abschlusspräsentation
Die Präsentation ist auf etwa 5–7 Minuten pro Gruppe angesetzt. Sie sollte folgende Aspekte enthalten:

- Funktionsübersicht des Systems (ggf. als Live-Demo)
- Erklärung der OOP-Umsetzung: Vererbung, Konstruktoren, Klassenmethoden
- Reflexion über Herausforderungen & Teamarbeit
- ggf. Erweiterungsideen für das System

## 📅 Zeitplanübersicht (Vorschlag)

| Stunde | Inhalt |
|--------|--------------------------------------------------------------------------|
| 1–2    | Projektstart, Gruppenbildung, Scrum-Einführung, User-Stories analysieren, Tasks ableiten |
| 3–4    | Umsetzung der Grundstruktur (Vererbung, Basisklassen, erste Methoden)    |
| 5–6    | Erweiterung, Klassenattribute/-methoden, Benutzeraktionen                |
| 7      | Testphase, Dokumentation (README), Präsentation vorbereiten              |
| 8      | Kundenpräsentation & Abschlussfeedback                                   |

*Zuletzt geändert: Sonntag, 25. Mai 2025, 20:58*
