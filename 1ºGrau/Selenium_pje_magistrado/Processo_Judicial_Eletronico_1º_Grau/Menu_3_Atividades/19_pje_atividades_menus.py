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
# 
driver.find_element(By.ID, "username").send_keys("05521677461")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("123")
time.sleep(2)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Atividades')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(), 'Avisos')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Consulta pessoa')]")

time.sleep(1000)