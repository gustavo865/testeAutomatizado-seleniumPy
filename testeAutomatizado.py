from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

# *** VARIABLES
executable_path = r'./chromedriver_win32/chromedriver.exe'
strUrl = 'https://www.google.com'
strTextToSearch = "UnimetrocampWyden"


# *** Drivers
driver = webdriver.Chrome(executable_path)

# *** STEP 01: Abre o browser e carrega a URL 
driver.get(strUrl)

# *** STEP 02: Check if the Object was found successfully
isOk = driver.find_element_by_name('q')

if isOk:
    print('STEP 01: Campo Search foi encontrado com sucesso')
else:
    print('STEP 01: Campo Search não foi encontrado com sucesso')


# *** STEP 03: Type some information in the Search field
driver.find_element_by_name('q').send_keys(strTextToSearch + Keys.ENTER)

validacaoDeBusca = driver.find_elements_by_xpath('//*[@id="tads"]/div[1]/div/div/div/div[1]/a/div[1]/span')

if validacaoDeBusca:
    print('Busca encontrada com sucesso')
else:
    print('Busca não encotrada')
 

# *** STEP 03: Endereço de um elemento HTML e clicka
driver.find_element_by_xpath('//*[@id="tads"]/div[1]/div/div/div/div[1]/a/div[1]/span').click()
time.sleep(2)

