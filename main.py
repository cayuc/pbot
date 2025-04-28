import time
import os
import subprocess
from flask import Flask
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Flask-server for keep alive
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def install_chrome():
    subprocess.run('apt-get update', shell=True, check=True)
    subprocess.run('apt-get install -y chromium-browser', shell=True, check=True)

def login_and_fill():
    print("Starter nettleser...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome(options=chrome_options)

    try:
        wait = WebDriverWait(driver, 20)

        print("Åpner nettsiden...")
        driver.get("https://pservice-permit.giantleap.no/visitor.html#/login")

        print("Logger inn...")
        wait.until(EC.presence_of_element_located((By.ID, "mat-input-0"))).send_keys("1138")
        wait.until(EC.presence_of_element_located((By.ID, "mat-input-1"))).send_keys("1138")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(),'Logg inn')]"))).click()

        print("Starter parkering...")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Start parkering')]"))).click()

        print("Fyller inn bilnummer...")
        wait.until(EC.presence_of_element_located((By.ID, "mat-input-2"))).send_keys("EH34234")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Neste')]"))).click()

        print("Bekrefter bil...")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Ja')]"))).click()

        print("Fyller inn e-post...")
        wait.until(EC.presence_of_element_located((By.ID, "mat-input-3"))).send_keys("bendik.johannessen@outlook.com")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Neste')]"))).click()

        print("Velger 6 timer parkering...")
