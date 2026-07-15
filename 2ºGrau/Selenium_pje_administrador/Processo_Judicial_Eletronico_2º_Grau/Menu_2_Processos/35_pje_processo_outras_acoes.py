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
driver.find_element(By.XPATH, "//a[contains(text(), 'Processo')]").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Outras ações").click()

time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(), 'Ajustar movimentação')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Associar processos')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Chamar à ordem')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Criar lote de processos')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'DJEN')]")
driver.find_element(By.XPATH, "//a[contains(normalize-space(), 'DJEN')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Enviar Processo')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Incluir alerta')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Incluir informação criminal relevante')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Incluir no push')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Liberar visualização de documentos')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Retificar autuação')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Peticionar')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Solicitar habilitação')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Peticionamento avulso')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Incluir processo(s) em rotina paralela')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Fechar tarefa aberta')]")



time.sleep(1000)