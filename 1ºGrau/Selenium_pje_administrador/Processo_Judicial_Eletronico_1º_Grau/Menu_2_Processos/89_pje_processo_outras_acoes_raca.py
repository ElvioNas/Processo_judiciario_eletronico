from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações básicas do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Inicializa o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

time.sleep(2)

#Realizando Login no sistema#

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("tjpe1977")
time.sleep(1)
driver.find_element(By.ID, "kc-login").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Processo')]").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Outras ações").click()

time.sleep(2)


driver.find_element(By.XPATH, "//a[contains(text(), 'Retificar autuação')]").click()

driver.find_element(By.XPATH, "//label[contains(text(), 'Número do Processo')]")
driver.find_element(By.XPATH, "//label[contains(text(), 'Nome da Parte')]")

driver.find_element(By.XPATH, "//input[contains(@id, 'idNumeroSequencial')]").send_keys("0000161")
driver.find_element(By.XPATH, "//input[contains(@id, 'idNumeroDigitoVerificador')]").send_keys("67")
driver.find_element(By.XPATH, "//input[contains(@id, 'idAno')]").send_keys("2024")
driver.find_element(By.XPATH, "//input[contains(@id, 'idNumeroOrigemProcesso')]").send_keys("5030")
driver.find_element(By.XPATH, "//input[contains(@value, 'Pesquisar')]").click()
time.sleep(5)
driver.find_element(By.ID, "consultaProcessoRetificacaoAutuacaoGridList:0:j_id241:j_id242:j_id244").click()
time.sleep(8)
#driver.find_element(By.XPATH, "//td[text()='Partes']").click()
#driver.find_element(By.XPATH, "//td[contains(text(), 'Partes')]").click()

#driver.find_element(By.ID, "tabPartes_lbl").click()
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/Processo/RetificacaoAutuacao/updateRetificacaoAutuacao.seam?idProcesso=6188959&tab=form")



#driver.find_element(By.ID, "tabPartes_lbl").click()

driver.find_element(By.XPATH, "//td[contains(text(), 'Partes')]").click()
time.sleep(5)

#driver.find_element(By.XPATH, "//a[contains(text(), 'Editar)]").click()


time.sleep(1000)