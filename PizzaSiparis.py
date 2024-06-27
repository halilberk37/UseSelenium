import time
import cv2
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan
driver.get("https://tomspizzeria.b4a.app/")


def siparisver():
    driver.find_element(By.ID,"siparis").click()

def mesajOku():
    return driver.find_element(By.ID,"mesaj").text


# Musteri isim
siparisver()
mesaj = mesajOku()
assert mesaj == "Müşteri ismi girmediniz"
# Müsteri ismi girmediniz

# Pizza Boyu

# Pizza boyu seçmediniz.
isim = "Tom Cruise"
driver.find_element(By.ID,"musteri-adi").send_keys(isim)
siparisver()
mesaj = mesajOku()
assert mesaj=="Pizza boyu seçmediniz"

# Ödeme Şekli


# Ödeme tipi seçilmedi
driver.find_element(By.CSS_SELECTOR,"input[value='Küçük']").click()
siparisver()
mesaj = mesajOku()
assert mesaj == "Ödeme tipi seçmediniz"


# Sipariş Alındı
dropdown = driver.find_element(By.ID,"odeme-tipi")
odeme = Select(dropdown)
odeme.select_by_index(2)
siparisver()
mesaj = mesajOku()
assert mesaj == "Siparişiniz alındı"


# Sipariş Bilgileri






'''isim_kutusu = driver.find_element(By.ID,"musteri-adi")
isim_kutusu.send_keys("Halil İbrahim BERK")

orta_boy = driver.find_element(By.XPATH,'//*[@id="select-size"]/div/div/div[2]/input')
orta_boy.click()

mısır_kutusu = driver.find_element(By.XPATH,'//*[@id="select-topping"]/div/div/div[4]/input')
mısır_kutusu.click()'''





input("Wait")