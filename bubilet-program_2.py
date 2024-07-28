import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# E-posta gönderimi için ayarlar
def send_email(subject, body, to_email):
    from_email = 'your_email@example.com'  # Kendi e-posta adresinizi girin
    from_password = 'your_password'  # Kendi e-posta şifrenizi girin

    # E-posta ayarları
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # E-posta gönderimi
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# WebDriver'ı başlatma
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL'yi açın
url = 'https://www.bubilet.com.tr/istanbul?sehir=istanbul&gad_source=1&gclid=CjwKCAjw2Je1BhAgEiwAp3KY78ZxGmE-xg5qB4Cmm9bjWLiViwqtxjWYtQOhiKSnJTECAw-dmUeTbhoCZhMQAvD_BwE'  # Değiştirmeniz gereken URL
driver.get(url)

# Sayfanın tamamen yüklenmesini bekleyin
time.sleep(5)

# Belirli sınıfa sahip div'i bulma
div_element = driver.find_element(By.CLASS_NAME, 'events.grid-list-4.ng-star-inserted')

# div elementinin altındaki tüm 'a' etiketlerini bulma
a_elements = div_element.find_elements(By.TAG_NAME, 'a')

# 'Ata Demirer Gazinosu' başlıklı 'a' etiketine tıklama
for a_element in a_elements:
    title = a_element.get_attribute('title')
    if title == "Ata Demirer Gazinosu":
        a_element.click()
        break

# Tıklamadan sonra 15 saniye bekleme
time.sleep(15)

# E-posta gönderme
subject = 'Ata Demirer Gazinosu Bileti'
body = 'Ata Demirer Gazinosu bulundu ve biletler mevcut.'
to_email = 'recipient@example.com'  # Alıcı e-posta adresini girin
send_email(subject, body, to_email)

# Tarayıcıyı kapatma
driver.quit()

print("Link with title 'Ata Demirer Gazinosu' has been clicked and waited for 15 seconds, email sent.")
