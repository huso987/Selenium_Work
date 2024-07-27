from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# WebDriver'ı başlatma
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL'yi açın
url = 'https://www.instagram.com/'
driver.get(url)
time.sleep(5)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("write_your_username")
password.send_keys("write_your_password")

giris = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
giris.click()

time.sleep(30)
driver.close()