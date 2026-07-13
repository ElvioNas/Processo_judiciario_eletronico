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
# FUNÇÃO CONTADOR
# ==============================
def contar(by, valor, acao=None, texto=None):
    global contador, sucessos, falhas
    contador += 1
    
    try:
        elemento = driver.find_element(by, valor)
        
        if acao == "click":
            elemento.click()
        elif acao == "send_keys":
            elemento.send_keys(texto)
        
        sucessos += 1
        print(f"[{contador}] ✔ OK -> {valor}")
        return elemento
        
    except Exception as e:
        falhas += 1
        print(f"[{contador}] ✖ FALHOU -> {valor}")
        print(f"    Erro: {e}")
        return None


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
contar(By.ID, "username", "send_keys", "02112357417")
time.sleep(1)

contar(By.ID, "password", "send_keys", "tjpe1977")
time.sleep(1)

contar(By.ID, "btnEntrar", "click")
time.sleep(1)


# ==============================
# MENU
# ==============================
contar(By.CLASS_NAME, "botao-menu", "click")
time.sleep(1)

contar(By.XPATH, "//a[contains(text(), 'Atividades')]", "click")
time.sleep(2)

contar(By.PARTIAL_LINK_TEXT, "Avisos", "click")


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