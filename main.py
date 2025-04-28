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
