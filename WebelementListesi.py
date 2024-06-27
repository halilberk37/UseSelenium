from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service) # bana bir chrome driver aç ve belirttiğim adresteki chrome driveri kullan
driver.get("https://imdb.com")
driver.maximize_window()
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span').click()
# film_isimleri = driver.find_elements(By.XPATH,"//table/tbody//tr//td[@class='titleColumn']")
film_isimleri = driver.find_elements(By.XPATH,'//*[@id="main"]/div/span/div[1]/div/div[3]/table/tbody/tr//td[@class="titleColumn"]')

#Hata alıyorum.
for i in range(20):
    print(film_isimleri[i].text)






input("Waitt")