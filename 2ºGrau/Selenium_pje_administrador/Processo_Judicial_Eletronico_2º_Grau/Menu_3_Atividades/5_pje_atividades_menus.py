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
# 
driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("123")
time.sleep(2)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Atividades')]").click()
time.sleep(2)
#driver.find_element(By.PARTIAL_LINK_TEXT, "Painel do representante processual").click()

driver.find_element(By.XPATH, "//a[contains(text(), 'Assinar documentos pendentes')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Avisos')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Consulta pessoa')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Criar relação pessoal')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Desunificar pessoas')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Distribuição de expediente')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Emitir certidão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Impressão de documento em lote')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pauta de perícia')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Redistribuição de expediente')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Registrar disponibilidade de perito')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Registrar indisponibilidade de perito')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Requisição de antecipação de pagamento do perito')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Elaborar RPV ou precatório')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Imprimir RPV e precatório')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Simular valor a compensar')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Solicitação de antecipação de pagamento de perícia')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Consultar Mandados')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Baixar arquivo de contatos para o SPE Escritório')]")

time.sleep(1000)