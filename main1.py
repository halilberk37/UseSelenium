from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan
driver.get("http://www.apple.com") # ben çalıştığımda nereye gideyim bana link ver!
baslik = driver.current_url
print("Suanki baslik: "+ baslik)

driver.get("http://www.etsy.com")
baslik = driver.current_url
print("Suanki baslik: "+ baslik)
title = driver.title
print(title)
driver.back()
baslik = driver.title
print(baslik)
#şu anki pencereyi kapatır.
driver.close()
#driver.quit() tüm sekmeleri kapatır

input("Wait")
