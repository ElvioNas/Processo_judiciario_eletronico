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

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("123")
time.sleep(2)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Audiências e sessões')]").click()
time.sleep(2)

#driver.find_element(By.XPATH, "//a[contains(text(), 'Acórdão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Cadastro de sessão de julgamento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Decisão de julgamento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Tipo de julgamento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Parâmetro')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pauta de audiência')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Publicação de decisões em sessão / em mural')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pendências da sessão de julgamento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Processos pautados em sessão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Relação de julgamento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pauta de julgamento')]")

time.sleep(1000)
