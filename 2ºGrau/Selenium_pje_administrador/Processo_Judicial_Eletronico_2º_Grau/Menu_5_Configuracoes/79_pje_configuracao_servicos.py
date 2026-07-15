from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam")



time.sleep(2)

#Realizando Login no sistema#

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("123")
time.sleep(1)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Configuração')]").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Serviços").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Criminal')]")
#time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Bacen')]")
#time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'ECarta')]")
#time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'MNI Client')]")
#time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Renajud')]")


time.sleep(1000)