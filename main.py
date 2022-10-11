from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
option = Options()
option.headless = True
driver = webdriver.Chrome(PATH,options=option)

driver.get('https://www.comparefirst.sg/wap/homeEvent.action')


try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located(
        By.XPATH, "//select[@name='coverageTermTLDCIPs']"
    ))
    find_term = driver.find_element(By.XPATH, "//select[@name='coverageTermTLDCIPs']")
    select = Select(find_term)
    all_selected_options = select.all_selected_options
    options = select.options[1]
    print('\n'+options.get_attribute('text'))
    print("Success")
except: 
    print("Error gan")
driver.quit()