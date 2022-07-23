# buecherhallenScraper
Ein Scraper in Python, der eine Liste von Büchern in einer Liste von Hamburger Bücherhallen durchgeht und bei Verfügbarkeit eine SMS schickt. 
Für die SMS wird die API von MessageBird verwendet.
Der Scraper ist extrem simpel und durchsucht schlicht den Seitenquelltext, den buecherhallen.de pro Buch mit der Verfügbarkeit je Bücherhalle ausgibt.

Vor Nutzung des Scipts mit einem verfügbaren und einem nicht verfügbaen Buch testen, denn wenn sich der Seitenaufbau ändert funktioniert die regular expression ggf. nicht mehr.

Pull requests für eine bessere regex oder bessere Fehlerbehandlung nehme ich gerne entgegen :- )
