from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def start_browser():
    """Startet den Browser und gibt den Treiber zurück."""
    driver_path = "Pfad/zum/chromedriver"  # Pfad zu deinem ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximierter Browser
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    return driver

def login_to_tiktok(driver, username, password):
    """Loggt sich bei TikTok ein."""
    print("Öffne TikTok und führe Login durch...")
    driver.get("https://www.tiktok.com/login")
    time.sleep(5)  # Warten, bis die Seite vollständig geladen ist

    # Eingabefelder für Benutzername und Passwort finden
    username_field = driver.find_element(By.NAME, "username_or_email")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login-Button klicken
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Zeit geben, um Login-Prozess abzuschließen
    time.sleep(10)
    print("Login abgeschlossen!")

def switch_to_new_stream(driver):
    """Springt zu einem neuen Livestream."""
    print("Springe zu einem neuen Livestream...")
    try:
        # Suche nach einem "Nächster Livestream"-Button oder Ähnlichem
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'next-livestream-button')]"))
        )
        next_button.click()
    except:
        # Alternativ: Öffne erneut die Livestream-Seite
        driver.get("https://www.tiktok.com/live")
        time.sleep(random.randint(3, 6))  # Zufällige Wartezeit
    print("Neuer Livestream geladen!")

def wait_and_open_box(driver):
    """Wartet auf das Ende des Kistentimers und öffnet die Kiste."""
    print("Suche nach Kisten...")
    try:
        # Suche nach der Kiste
        box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'reward-box')]"))
        )

        # Prüfen, ob die Kiste sofort geöffnet werden kann oder ein Timer läuft
        while True:
            try:
                box.click()  # Kiste öffnen
                print("Kiste geöffnet!")
                time.sleep(3)  # Wartezeit, um sicherzustellen, dass die Kiste geöffnet ist
                break
            except Exception as e:
                print("Kiste kann noch nicht geöffnet werden, warte...")
                time.sleep(60)  # Warte eine Minute und überprüfe erneut
    except Exception as e:
        print("Keine Kiste gefunden oder verfügbar:", e)

def tiktok_bot(username, password):
    """Startet den TikTok-Bot."""
    driver = start_browser()  # Browser starten
    
    try:
        login_to_tiktok(driver, username, password)  # Login durchführen
        
        # Navigiere zu Livestreams
        driver.get("https://www.tiktok.com/live")
        time.sleep(5)

        # Endlosschleife für Livestreams
        while True:
            wait_and_open_box(driver)  # Warten und Kiste öffnen
            switch_to_new_stream(driver)  # Zum nächsten Stream springen

    except Exception as e:
        print("Ein Fehler ist aufgetreten:", e)
    finally:
        driver.quit()  # Browser schließen

# Daten des Nutzers abfragen
print("Willkommen beim TikTok Livestream-Bot!")
username = input("Gib deinen TikTok-Benutzernamen oder deine E-Mail ein: ")
password = input("Gib dein TikTok-Passwort ein: ")

# Bot starten
tiktok_bot(username, password)
