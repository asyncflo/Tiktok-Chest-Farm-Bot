# Tiktok-Chest-Farm-Bot
Der TikTok Livestream-Bot ist ein Python-Skript, das mit Selenium automatisiert TikTok-Livestreams durchsucht. Nach dem Einloggen sucht der Bot in jedem Livestream nach Kisten (z. B. Belohnungsboxen). Wenn eine Kiste gefunden wird, überprüft er, ob sie geöffnet werden  kann.
Login automatisiert:
Du gibst deinen TikTok-Benutzernamen und dein Passwort direkt im Terminal ein, und der Bot loggt sich automatisch ein.
Warten auf Kisten-Timer:
Der Bot überprüft, ob die Kiste geöffnet werden kann. Wenn nicht, wartet er 60 Sekunden und überprüft erneut. Dies geschieht in einer Schleife, bis die Kiste geöffnet wird.
Springen zu neuen Livestreams:
Nachdem eine Kiste geöffnet wurde oder keine Kiste gefunden wurde, wechselt der Bot automatisch zum nächsten Livestream.
Unendlich laufender Bot:
Die Schleife läuft unbegrenzt weiter. Du kannst den Bot jederzeit beenden, indem du das Programm im Terminal stoppst (z. B. mit Strg+C).
Menschliches Verhalten:
Der Bot verwendet zufällige Wartezeiten (random.randint(3, 6)), um menschlicher zu wirken.


If you need any help hit me up on discord @59bby
