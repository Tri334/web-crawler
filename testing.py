from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
PATH = 'C:\Program Files (x86)\chromedriver.exe'
option = Options()
option.headless = False
driver = webdriver.Chrome(PATH,options=option)

driver.get('https://www.comparefirst.sg/wap/homeEvent.action')


## Select Category
def selectCategory():
    try:
        driver.implicitly_wait(2)
        search = driver.find_element(By.ID,"bips").click()
        driver.implicitly_wait(2)

        ## click Whole Life
        # select_category = 
        driver.find_element(By.XPATH,"//ul[@id='bips-option']//li[@data-id='whole-life']").click()
        sleep(2)
        ## click Term Life
        # select_category = 
        driver.find_element(By.XPATH,"//ul[@id='bips-option']//li[@data-id='term-life']").click()    
        print('success'.center(20))
    except:
        print('Error'.center(20))


## Select DateOfBirth
def selectDateOfBirth():
    try:
        ##remember the //*
        date = driver.find_element(By.XPATH,"//*[@id='date']")
        return date.send_keys('30/10/1999')
    except:
        return print('An exception occurred')


## Select Gender
def selectGender():
    try:
        driver.find_element(By.XPATH,"//ul[@class='gender']//li[@data-id='M']").click()
        sleep(5)
        driver.find_element(By.XPATH,"//ul[@class='gender']//li[@data-id='F']").click()
    except:
        print('Element not found')

def selectSmoker():
    try:
        driver.find_element(By.XPATH,"//ul[@id='smoker']//li[@data-id='Y']").click()
        sleep(5)
        driver.find_element(By.XPATH,"//ul[@id='smoker']//li[@data-id='N']").click()
    except:
        print('Element not found')


#//*[@id="select2-chosen-14"]
tes1 = '20 Years'
# find_term_option = driver.find_element(By.XPATH,"//select[@name='coverageTermTLDCIPs']")
driver.maximize_window()
ele = driver.find_element(By.ID,'coverageTermTLDCIPs')
driver.execute_script('arguments[0].style.display = "block";', ele)
selectDateOfBirth()
WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.ID,"coverageTermTLDCIPs")))
# sleep(3)
find_term_option = driver.find_element(By.NAME,"coverageTermTLDCIPs")
for item in find_term_option.find_elements(By.TAG_NAME,'option'):
    # print(item.get_attribute('value'))
    value = item.get_attribute('value').strip()
    if tes1.strip() in value:
        item.click()
        print(tes1)
    else:
        print(value)
        print(tes1)
print('OK')
sleep(40)
driver.quit()
# Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='user']")))).select_by_value('7183')