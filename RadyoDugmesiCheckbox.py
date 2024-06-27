from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")

orta_boy = driver.find_element(By.CSS_SELECTOR,"input[value='Orta']")
zeytin = driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
mantar = driver.find_element(By.CSS_SELECTOR,"input[value='mantar']")
print(zeytin.is_selected())
print(mantar.is_selected())
print(orta_boy.is_selected())

orta_boy.click()
zeytin.click()
mantar.click()
print(zeytin.is_selected())
print(mantar.is_selected())
print(orta_boy.is_selected())


input("wait")