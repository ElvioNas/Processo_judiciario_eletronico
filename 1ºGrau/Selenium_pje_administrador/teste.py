from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")  # Ignora erros SSL
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Aguarda página carregar
driver.set_page_load_timeout(30)

try:
    print("Acessando site...")
    driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")
    print("Site acessado!")
    
    # Aguarda elementos carregarem
    time.sleep(5)
    
    print(f"Título: {driver.title}")
    print(f"URL atual: {driver.current_url}")
    
except Exception as e:
    print(f"Erro: {e}")
    
time.sleep(1000)