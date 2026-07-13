from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
import time

# ==============================
# CONTADORES
# ==============================
contador = 0
sucessos = 0
falhas = 0

# ==============================
# FUNÇÃO CONTAR
# ==============================
def contar(descricao, funcao):
    global contador, sucessos, falhas
    contador += 1
    
    try:
        funcao()
        sucessos += 1
        print(f"[{contador}] ✔ OK -> {descricao}")
    except Exception as e:
        falhas += 1
        print(f"[{contador}] ✖ FALHOU -> {descricao}")
        print(f"     Erro: {e}")


# ==============================
# CONFIGURAÇÃO DO CHROME
# ==============================

chrome_options = Options()

chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")
time.sleep(2)

# ==============================
# LOGIN
# ==============================
contar("Digite o usuário", lambda: driver.find_element(By.ID, "username").send_keys("02112357417"))
time.sleep(1)

contar("Digite a senha", lambda: driver.find_element(By.ID, "password").send_keys("tjpe1977"))
time.sleep(1)

contar("Clique no botão login", lambda: driver.find_element(By.ID, "btnEntrar").click())
time.sleep(1)

# ==============================
# MENU
# ==============================
contar("Clique no menu principal", lambda: driver.find_element(By.CLASS_NAME, "botao-menu").click())
time.sleep(1)

contar("Clique em Processo", lambda: driver.find_element(By.XPATH, "//a[contains(text(), 'Processo')]").click())
time.sleep(2)

contar("Clique em Não protocolado", lambda: driver.find_element(By.PARTIAL_LINK_TEXT, "Não protocolado").click())

# ==============================
# RELATÓRIO FINAL
# ==============================
print("\n==============================")
print(f"Total de etapas : {contador}")
print(f"Sucessos        : {sucessos}")
print(f"Falhas          : {falhas}")

if contador > 0:
    print(f"Taxa de sucesso : {(sucessos/contador)*100:.2f}%")

print("==============================")

time.sleep(1000)