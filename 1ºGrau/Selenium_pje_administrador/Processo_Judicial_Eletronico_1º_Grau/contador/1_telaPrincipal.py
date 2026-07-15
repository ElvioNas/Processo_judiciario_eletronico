from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# ==============================
# CONTADORES
# ==============================

total = 0
sucessos = 0
falhas = 0

def validar_texto(xpath, texto_esperado):
    global total, sucessos, falhas

    total += 1

    try:
        elemento = driver.find_element(By.XPATH, xpath)

        assert elemento.text.strip() == texto_esperado

        sucessos += 1
        print(f"[{total}] ✔ OK -> {texto_esperado}")

    except Exception:
        falhas += 1
        print(f"[{total}] ✖ FALHA -> {texto_esperado}")


# ==============================
# CONFIGURAÇÃO DO CHROME
# ==============================

chrome_options = Options()

chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

time.sleep(2)

# ==============================
# VALIDAÇÕES
# ==============================

validar_texto("//span[contains(text(),'Processo Judicial Eletrônico')]", "Processo Judicial Eletrônico")
validar_texto("//a[contains(text(),'Formas de acesso')]", "Formas de acesso")
validar_texto("//a[contains(text(),'Consulta processual')]", "Consulta processual")
validar_texto("//a[contains(text(),'Push')]", "Push")
validar_texto("//a[contains(text(),'Manuais')]", "Manuais")
validar_texto("//a[contains(text(),'Fale conosco')]", "Fale conosco")
validar_texto("//p[contains(text(),'Processo Judicial Eletrônico 1º Grau')]", "Processo Judicial Eletrônico 1º Grau")
validar_texto("//p[contains(text(),'Poder Judiciário de Pernambuco')]", "Poder Judiciário de Pernambuco")
validar_texto("//a[contains(text(),'Solicitar nova senha')]", "Solicitar nova senha")
validar_texto("//a[contains(text(),'Saiba como obter o certificado digital')]", "Saiba como obter o certificado digital")

# ==============================
# RELATÓRIO
# ==============================

print("\n==============================")
print("RELATÓRIO FINAL")
print("==============================")
print(f"Total verificações: {total}")
print(f"Sucessos: {sucessos}")
print(f"Falhas: {falhas}")

if total:
    print(f"Taxa de sucesso: {(sucessos/total)*100:.2f}%")

print("==============================")

time.sleep(1000)
driver.quit()