from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# WebDriver'ı başlatma
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL'yi açın
url = 'https://bigpara.hurriyet.com.tr/doviz/'
driver.get(url)
time.sleep(25)

# 'tBody' sınıfına sahip div'i bulun
try:
    tbody_div = driver.find_element(By.CLASS_NAME, "tBody")
except Exception as e:
    print(f"Error finding 'tBody' div: {e}")
    driver.quit()
    exit()

# 'tBody' div içindeki tüm 'ul' etiketlerini bulun
ul_elements = tbody_div.find_elements(By.TAG_NAME, "ul")

# Başlıkların listesi
headings = ["Döviz Cinsi", "Alış", "Satış", "Değişim %", "Saat"]

# Başlıkların ve içeriklerin yazdırılması
print(f"{'Döviz Cinsi':<20} {'Alış':<10} {'Satış':<10} {'Değişim %':<10} {'Saat':<10}")
print("="*60)  # Separator line

for ul in ul_elements:
    lines = ul.text.split('\n')
    for i in range(0, len(lines), 4):
        if i + 3 < len(lines):
            currency = lines[i].strip()
            alış = lines[i+1].strip()
            satış = lines[i+2].strip()
            değişim = lines[i+3].strip()
            saat = lines[i+4].strip() if (i+4) < len(lines) else ''
            print(f"{currency:<20} {alış:<10} {satış:<10} {değişim:<10} {saat:<10}")

# Tarayıcıyı kapatın
driver.quit()
