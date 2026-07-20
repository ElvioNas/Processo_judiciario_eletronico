from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


@given('que o sistema PJe 1º Grau está disponível')
def step_sistema_disponivel(context):
    """Verifica se o sistema está disponível"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")
    time.sleep(2)


@given('eu estou na tela principal de login')
def step_na_tela_login(context):
    """Valida que estamos na tela de login"""
    assert "PJe" in context.driver.title or "login" in context.driver.page_source.lower()


@when('eu faço login com usuário "{username}" e senha "{password}"')
def step_fazer_login(context, username, password):
    """Realiza login no sistema"""
    context.driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    context.driver.find_element(By.ID, "btnEntrar").click()
    time.sleep(2)


@when('eu clico no menu principal')
def step_clicar_menu_principal(context):
    """Clica no botão de menu principal"""
    context.driver.find_element(By.CLASS_NAME, "botao-menu").click()
    time.sleep(2)


@when('eu seleciono a opção "{menu_option}"')
def step_selecionar_menu(context, menu_option):
    """Seleciona uma opção específica do menu"""
    opcao_xpath = f"//a[contains(text(), '{menu_option}')]"
    context.driver.find_element(By.XPATH, opcao_xpath).click()
    time.sleep(2)


@when('eu clico em "{elemento_texto}"')
def step_clicar_elemento(context, elemento_texto):
    """Clica em um elemento identificado pelo texto"""
    try:
        elemento = context.driver.find_element(By.PARTIAL_LINK_TEXT, elemento_texto)
    except:
        elemento = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{elemento_texto}')]")
    elemento.click()
    time.sleep(2)


@then('eu devo ver a seção de "{secao}"')
def step_validar_secao(context, secao):
    """Valida que uma seção específica está visível"""
    elemento = context.driver.find_element(By.XPATH, f"//td[contains(text(), '{secao}')]")
    assert elemento.is_displayed()


@then('eu devo visualizar os seguintes filtros de expediente:')
def step_validar_filtros_expediente(context):
    """Valida que todos os filtros de expediente estão visíveis"""
    filtros = [row['Filtro'] for row in context.table]
    
    for filtro in filtros:
        elemento = context.driver.find_element(By.XPATH, f"//span[contains(text(), '{filtro}')]")
        assert elemento.is_displayed(), f"Filtro '{filtro}' não está visível"


@then('o campo de "{campo}" deve estar visível na tela')
def step_campo_visivel(context, campo):
    """Valida que um campo específico está visível"""
    if campo == "Expedientes":
        elemento = context.driver.find_element(By.XPATH, f"//td[contains(text(), '{campo}')]")
        assert elemento.is_displayed()


def teardown(context):
    """Limpa após o teste"""
    if hasattr(context, 'driver'):
        context.driver.quit()
