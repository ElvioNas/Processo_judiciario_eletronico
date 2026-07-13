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
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel')]").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Painel de expedientes").click()
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), ' Mostrar expedientes já impressos? ')]")
driver.find_element(By.XPATH,"//div[contains(text(), 'Meus Expedientes')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Número do Processo')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Expediente')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Urgente')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Data de Cadastro do Expediente')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Destinatário')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Imprimir')]")
driver.find_element(By.XPATH, "//form[contains(text(), 'Impresso?')]")

#time.sleep(2)

time.sleep(1000)