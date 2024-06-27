import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")

dropdown = driver.find_element(By.ID,"odeme-tipi")
odeme = Select(dropdown)

odeme_tipleri = odeme.options # web element listesi

for tip in odeme_tipleri:
    print(tip.text)
time.sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
time.sleep(2)
odeme.select_by_index(3)
time.sleep(2)
driver.quit()
