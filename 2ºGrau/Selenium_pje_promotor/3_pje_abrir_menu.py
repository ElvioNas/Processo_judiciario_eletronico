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

driver.find_element(By.ID, "username").send_keys("13799253807")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("123")
time.sleep(2)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(2)

#Validando Label no Menu#

driver.find_element(By.CLASS_NAME, "botao-menu").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Processo')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Atividades')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Audiências e sessões')]")
#driver.find_element(By.XPATH, "//a[contains(text(), 'Configuração')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Download')]")
time.sleep(1000)