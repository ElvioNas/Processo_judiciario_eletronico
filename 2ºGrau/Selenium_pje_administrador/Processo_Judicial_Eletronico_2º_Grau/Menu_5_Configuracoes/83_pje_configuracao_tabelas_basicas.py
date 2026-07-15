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
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Tabelas básicas").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Eleição')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Bairros')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Calendário')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'CEP')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Escolaridade')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Estado civil')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Especialização do Meio de Expedição')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Raça')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Profissão (CBO)')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Tipo de contrato')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Tipo de endereço')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Tipo do documento de identificação')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Tipo de relação pessoal')]")

time.sleep(1000)