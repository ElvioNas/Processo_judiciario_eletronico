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

driver.find_element(By.ID, "username").send_keys("62500716520")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("123")
time.sleep(2)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel')]").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Painel do representante processual").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[contains(text(), 'Novo processo')]").click()
time.sleep(2)
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/Processo/cadastrar.seam?newInstance=true")
driver.find_element(By.XPATH, "//span[contains(text(), 'Cadastro de processo')]")
driver.find_element(By.XPATH, "//td[contains(normalize-space(), 'Dados Iniciais')]")
driver.find_element(By.XPATH, "//label[contains(text(), 'Matéria')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'Jurisdição')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'Classe judicial')]")
time.sleep(1000)