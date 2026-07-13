from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")


time.sleep(2)

#Realizando Login no sistema#

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("tjpe1977")
time.sleep(1)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Configuração')]").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Motivos de Isenção").click()
driver.find_element(By.XPATH, "//label[contains(text(), 'Motivo de Isenção da Guia de Recolhimento')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Situação')]")
time.sleep(1)
driver.find_element(By.XPATH, "//td[contains(text(), 'Formulário')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'Campos obrigatórios')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Motivo de Isenção da Guia de Recolhimento')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Controla situação da guia')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Situação')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Sim')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Não')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Ativo')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Inativo')]")
time.sleep(1)




time.sleep(1000)