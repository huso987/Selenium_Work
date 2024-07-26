# Gerekli kütüphaneleri yükleyin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# ChromeDriver yolunu belirleyin ve Service nesnesini oluşturun
service = Service(ChromeDriverManager().install())

# WebDriver'ı başlatın (Service nesnesini kullanarak)
driver = webdriver.Chrome(service=service)

# GitHub kullanıcısının kullanıcı adını tanımlayın
username = 'huso987'  # Buraya kullanıcı adını yazın

# Kullanıcının GitHub profil sayfasına gidin
driver.get(f'https://github.com/{username}?tab=repositories')

time.sleep(3)  # Sayfanın yüklenmesi için bekleyin

# Verileri depolamak için boş bir liste oluşturun
data = []

# Sayfada yer alan projeleri ve dillerini toplayın
repositories = driver.find_elements(By.CLASS_NAME, 'source')
for repo in repositories:
    repo_name = repo.find_element(By.CLASS_NAME, 'wb-break-all').text
    try:
        repo_language = repo.find_element(By.XPATH, './/span[@itemprop="programmingLanguage"]').text
    except:
        repo_language = 'Not specified'
    
    data.append([repo_name, repo_language])

# Verileri bir DataFrame'e dönüştürün ve CSV dosyasına kaydedin
df = pd.DataFrame(data, columns=['Repository Name', 'Programming Language'])
df.to_csv('github_repositories.csv', index=False)

# WebDriver'ı kapatın
driver.quit()
