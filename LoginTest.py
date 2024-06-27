from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan

# test otomasyon

# internet login sayfasına git https://the-internet.herokuapp.com/login
driver.get("https://the-internet.herokuapp.com/login")
# kullancici adi gir
driver.find_element(By.ID,"username").send_keys("test")
# şifre gir
driver.find_element(By.ID,"password").send_keys("")
# login dugmesine tıkla
driver.find_element(By.CLASS_NAME,"radius").click()
#Yanlis kullanici adi: Your username is invalid
mesaj = driver.find_element(By.ID,"flash").text

if "Your username is invalid!" in mesaj:
    print("Ok, Doğru çalışıyor")
else:
    print("hata düzgün çalışmıyor")

# yanlis sifre girince: Your password is invalid!
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("asda")
driver.find_element(By.CLASS_NAME,"radius").click()
mesaj2 = driver.find_element(By.ID,"flash").text

if "Your password is invalid!" in mesaj:
    print("Ok, Doğru çalışıyor")
else:
    print("hata düzgün çalışmıyor")

# ikisi de doğru ise
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME,"radius").click()
mesaj3 = driver.find_element(By.ID,"flash").text

if "You logged into a secure area!" in mesaj:
    print("Ok, Doğru çalışıyor")
else:
    print("hata düzgün çalışmıyor")

link = driver.current_url
if "secure" in link:
    print("Ok link secure içeriyor")
else:
    print("hata: link secure içermiyor")

#logout dugmesine tıkla
driver.find_element(By.XPATH,"//i[contains(text(),'Logout')]").click()

#sayfa linkini dogrula
if "login" in driver.current_url:
    print("Ok. login sayfasina donduk")
else:
    print("hata : login sayfasina dönmedi")

driver.quit()

input("Wait")




'''
userName = "tomsmith"
password = "SuperSecretPassword!"


userNameKutusu = driver.find_element(By.ID,"username")
userNameKutusu.send_keys(userName)

passwordKutusu = driver.find_element(By.ID,"password")
passwordKutusu.send_keys(password)

loginButonu = driver.find_element(By.CLASS_NAME,"radius").click()

Kendi çözümüm.

'''

