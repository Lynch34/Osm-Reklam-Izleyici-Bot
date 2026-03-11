from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

username = "YourUserNameHere"
password = "YourPasswordHere"

driver = webdriver.Chrome()
url = "https://en.onlinesoccermanager.com/Login"
driver.get(url)

time.sleep(3) # Login Sayfasi Bekleme

try:
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[3]/div/button').click()
    print("[DEBUG] Giriş tıklandı 1.")
    print("[DEBUG] 3 saniye bekleniyor.")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[4]/div[2]/button').click()
    print("[DEBUG] Giriş tıklandı 2")
    print("[DEBUG] 3 saniye bekleniyor.")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/form/div[1]/input').send_keys(username)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/form/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/form/button').click()
    print("[DEBUG] Giriş tıklandı 3.")
    print("[DEBUG] 10 saniye bekleniyor.")
    time.sleep(10)
    print("[DEBUG] URL açılıyor.")
    print("[DEBUG] 5 saniye bekleniyor.")
    driver.get("https://en.onlinesoccermanager.com/BusinessClub")
    time.sleep(5)

except NoSuchElementException:
    print("XPath bulunamadı. Elemente tıklanamadı.")

start_time = time.time()

while True:
    for i in range(1, 11):
        # Reklamı tıkla

        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div/div[2]/div[2]/div/div[1]/div').click()
            print("Reklama tıklandı.")
            time.sleep(40)
        except Exception as e:
            print(f"Reklam izlenmedi (E)")
            time.sleep(5)
        
        # Reklamı geç butonunu dene
        try:
            driver.find_element(By.XPATH, '/html/body/div[9]/div/button[2]').click()
            print("Reklam geç butonu bulundu ve tıklandı.")
            time.sleep(5)
        except Exception as e:
            print(f"Reklam izlenmedi (E)")
            time.sleep(5)
            
        # Reklam sürem bitti mi
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div/div[2]/div[4]/div/div/div/div[3]/div/div/div').click()
            print("Reklam izlenmedi.")
            time.sleep(60)
        except Exception as e:
            print(f"Reklam izlenmedi (E)")
            time.sleep(5)

    elapsed_time = time.time() - start_time
    if elapsed_time >= 3600:
        print("Sayfa yenileniyor...")
        driver.refresh()
        time.sleep(10)
        start_time = time.time()