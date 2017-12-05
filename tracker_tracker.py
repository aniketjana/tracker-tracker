from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from datetime import date
from datetime import datetime

url_file = [line.rstrip('\n') for line in open('url.txt')]
file = open("sokrati-"+str(date.today())+".txt", 'w')
for url in url_file:
    print('Searching for url: '+ url)
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

    driver = webdriver.Chrome('E:/chromedriver.exe',chrome_options=chrome_options)
    driver.get(url)
    delay = 10 # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//script[contains(@src,'https://tracking.sokrati.com/javascripts/tracker.js')]")))
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//script[contains(@src,'https://chuknu.sokrati.com/14899/tracker.js')]")))
        msg = "Sokrati pixels present, Bindass!"
        file.write(url + '\t' + msg + '\n' )    
        driver.quit()
       
    except TimeoutException:
        msg = "Sokrati pixels not present, Ram Ram!"
        file.write(url + '\t' + msg + '\n' )
        driver.quit()
file.close()
    
