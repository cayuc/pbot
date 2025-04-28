from flask import Flask
from keep_alive import keep_alive
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def login_and_fill():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://din-ekte-nettside.no/login")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mat-input-3"))
        ).send_keys("bendik.johannessen@outlook.com")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Neste')]"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-radio-button//div[contains(text(),'6 timer')]"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Neste')]"))
        ).click()

        print("Ferdig!")

    except Exception as e:
        print(f"En feil oppstod: {e}")

    finally:
        driver.quit()

# Hold serveren oppe
keep_alive()

# Hovedloop
while True:
    if os.path.exists("switch.txt"):
        with open("switch.txt", "r") as f:
            status = f.read().strip()

        if status == "ON":
            login_and_fill()
            print("Venter 6 timer og 3 minutter...")
            time.sleep((6 * 60 + 3) * 60)
        else:
            print("Bot er AV. Sjekker igjen om 1 minutt.")
            time.sleep(60)
    else:
        print("Fant ikke switch.txt, lager en ny som OFF...")
        with open("switch.txt", "w") as f:
            f.write("OFF")
