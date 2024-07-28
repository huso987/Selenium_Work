from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# WebDriver'ı başlatma
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL'yi açın
url = 'https://www.bubilet.com.tr/istanbul?sehir=istanbul&gad_source=1&gclid=CjwKCAjw2Je1BhAgEiwAp3KY78ZxGmE-xg5qB4Cmm9bjWLiViwqtxjWYtQOhiKSnJTECAw-dmUeTbhoCZhMQAvD_BwE'
driver.get(url)
time.sleep(15)

# Belirli sınıfa sahip div'i bulma
div_element = driver.find_element(By.CLASS_NAME, 'events.grid-list-4.ng-star-inserted')

# div elementinin altındaki tüm 'a' etiketlerini ve 'span' etiketlerini bulma
a_elements = div_element.find_elements(By.TAG_NAME, 'a')
span_elements = div_element.find_elements(By.CLASS_NAME, 'ng-star-inserted')

# Her bir 'a' etiketinin 'title' özniteliğini al ve yazdır
print("Titles:")
for element in a_elements:
    title = element.get_attribute('title')
    if title:  # Sadece 'title' özniteliği olanları yazdır
        print(title)

# Her bir 'span' etiketinin metin içeriğini al ve yazdır
print("\nDates:")
for element in span_elements:
    date = element.text
    if date:  # Sadece metin içeriği olanları yazdır
        print(date)

# izin = driver.find_element(By.XPATH, "//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
# izin.click()

time.sleep(30)
driver.close()