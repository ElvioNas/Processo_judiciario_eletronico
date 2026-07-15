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

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Processo')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Novo processo')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Novo processo incidental')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Não protocolado')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pesquisar')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Outras ações')]")
time.sleep(1000) 