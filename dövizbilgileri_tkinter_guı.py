import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import threading

def fetch_data():
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
        return []

    # 'tBody' div içindeki tüm 'ul' etiketlerini bulun
    ul_elements = tbody_div.find_elements(By.TAG_NAME, "ul")
    driver.quit()

    data = []

    for ul in ul_elements:
        lines = ul.text.split('\n')
        for i in range(0, len(lines), 4):
            if i + 3 < len(lines):
                currency = lines[i].strip()
                alış = lines[i + 1].strip()
                satış = lines[i + 2].strip()
                değişim = lines[i + 3].strip()
                saat = lines[i + 4].strip() if (i + 4) < len(lines) else ''
                data.append((currency, alış, satış, değişim, saat))

    return data

def update_treeview(data):
    # Clear existing data
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert new data
    for item in data:
        tree.insert("", tk.END, values=item)

def display_data():
    def run_fetch_data():
        data = fetch_data()
        if data:
            root.after(0, lambda: update_treeview(data))
    
    threading.Thread(target=run_fetch_data).start()

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("Döviz Kurları")

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

columns = ("Döviz Cinsi", "Alış", "Satış", "Değişim %", "Saat")
tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

button = tk.Button(root, text="Verileri Getir", command=display_data)
button.pack(pady=10)

root.mainloop()
