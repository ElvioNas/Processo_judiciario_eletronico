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
driver.find_element(By.PARTIAL_LINK_TEXT, "Painel do magistrado na sessão").click()
time.sleep(1)
#driver.find_element(By.ID,"//*[@id=]/div/div[1]/div/text(), 'Assinaturas')]")
#//*[@id="rightPanel"]/div/div[1]/div/text()
#driver.find_element(By.XPATH,"//div[contains(text(), 'Assinaturas')]")
#driver.find_element(By.XPATH, "//label[contains(text(), ' Mostrar expedientes já impressos? ')]")
#driver.find_element(By.XPATH,"//div[contains(text(), 'Meus Expedientes')]")
#driver.find_element(By.ID, "element_id, processoExpedienteSetorGridList:j_id178:j_id179")
#driver.find_element(By.XPATH, "//div[contains(text(), 'Número do Processo')]")
#time.sleep(2)

time.sleep(1000)