from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan
driver.get("http://www.duckduckgo.com") # ben çalıştığımda nereye gideyim bana link ver!

aramaKutusu = driver.find_element(By.ID,"search_form_input_homepage")
aramaKutusu.send_keys("python")
aramaKutusu.send_keys(Keys.ENTER)




input("Wait")