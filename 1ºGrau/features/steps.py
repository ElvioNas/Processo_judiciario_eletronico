# Arquivo de Definições de Passos (Steps) para Gherkin
# Instalação: pip install behave selenium
# Execução: behave features/

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# =============================================================================
# GIVEN - Pré-condições (Dado que...)
# =============================================================================

@given('que o navegador está aberto maximizado')
def step_open_browser(context):
    """Abre o navegador Chrome maximizado"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)

@given('que acesso a URL da tela inicial "{url}"')
def step_access_url(context, url):
    """Acessa uma URL específica"""
    context.driver.get(url)

@given('aguardar {seconds:d} segundos para carregar a página')
def step_wait_seconds(context, seconds):
    """Aguarda N segundos"""
    time.sleep(seconds)

@given('realizo login com as credenciais de administrador')
def step_login_admin(context):
    """Realiza login como administrador"""
    # Utilizar dados seguros (variáveis de ambiente)
    username = "02112357417"
    password = "tjpe1977"
    
    context.driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    context.driver.find_element(By.ID, "btnEntrar").click()
    time.sleep(3)

@given('realizo login com credenciais de administrador')
def step_login_as_admin(context):
    """Realiza login como administrador"""
    step_login_admin(context)

@given('realizo login com credenciais de advogado')
def step_login_as_lawyer(context):
    """Realiza login como advogado"""
    # Implementar com credenciais de advogado
    pass

@given('realizo login com credenciais de magistrado')
def step_login_as_judge(context):
    """Realiza login como magistrado"""
    # Implementar com credenciais de magistrado
    pass

@given('realizo login como administrador')
def step_login_admin_alt(context):
    """Realiza login como administrador (alternativa)"""
    step_login_admin(context)

@given('aguardo a página principal carregar completamente')
def step_wait_page_load(context):
    """Aguarda o carregamento completo da página"""
    time.sleep(3)

# =============================================================================
# WHEN - Ações (Quando...)
# =============================================================================

@when('preencho o campo "{field_id}" com "{value}"')
def step_fill_field(context, field_id, value):
    """Preenche um campo de texto"""
    field = context.driver.find_element(By.ID, field_id)
    field.clear()
    field.send_keys(value)

@when('aguardo {seconds:d} segundo')
def step_wait_second(context, seconds):
    """Aguarda 1 segundo"""
    time.sleep(seconds)

@when('aguardo {seconds:d} segundos')
def step_wait_multiple_seconds(context, seconds):
    """Aguarda N segundos"""
    time.sleep(seconds)

@when('clico no botão "{button_id}"')
def step_click_button(context, button_id):
    """Clica em um botão"""
    button = context.driver.find_element(By.ID, button_id)
    button.click()

@when('clico no link "{link_text}"')
def step_click_link(context, link_text):
    """Clica em um link"""
    link = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{link_text}')]")
    link.click()

@when('clico no menu "{menu_name}"')
def step_click_menu(context, menu_name):
    """Clica em um item de menu"""
    menu = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{menu_name}')]")
    menu.click()

@when('preencho o campo de busca com "{search_term}"')
def step_fill_search_field(context, search_term):
    """Preenche o campo de busca"""
    search = context.driver.find_element(By.XPATH, "//input[@placeholder='Buscar...' or @class='search-field']")
    search.clear()
    search.send_keys(search_term)

@when('pressiono Enter')
def step_press_enter(context):
    """Pressiona a tecla Enter"""
    from selenium.webdriver.common.keys import Keys
    context.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.RETURN)

@when('seleciono a primeira atividade da lista')
def step_select_first_activity(context):
    """Seleciona a primeira atividade"""
    activities = context.driver.find_elements(By.XPATH, "//div[@class='activity-item']")
    if activities:
        activities[0].click()

@when('clico no botão "Concluir"')
def step_click_complete_button(context):
    """Clica no botão Concluir"""
    button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Concluir')]")
    button.click()

@when('clico no processo encontrado')
def step_click_found_process(context):
    """Clica no processo encontrado na lista"""
    process = context.driver.find_element(By.XPATH, "//tr[@class='process-row'][1]")
    process.click()

# =============================================================================
# THEN - Validações (Então...)
# =============================================================================

@then('deve exibir o título "{title}"')
def step_verify_title(context, title):
    """Verifica se o título está visível"""
    element = context.driver.find_element(By.XPATH, f"//span[contains(text(), '{title}')]")
    assert element.text == title, f"Título '{title}' não encontrado"

@then('deve exibir o subtítulo "{subtitle}"')
def step_verify_subtitle(context, subtitle):
    """Verifica se o subtítulo está visível"""
    element = context.driver.find_element(By.XPATH, f"//p[contains(text(), '{subtitle}')]")
    assert element.text == subtitle, f"Subtítulo '{subtitle}' não encontrado"

@then('deve exibir "{text}"')
def step_verify_text(context, text):
    """Verifica se um texto está visível"""
    element = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
    assert text in element.text

@then('deve exibir o link "{link_text}"')
def step_verify_link_exists(context, link_text):
    """Verifica se um link está visível"""
    link = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{link_text}')]")
    assert link.is_displayed(), f"Link '{link_text}' não está visível"

@then('deve exibir o campo de entrada para "{field_id}"')
def step_verify_field_exists(context, field_id):
    """Verifica se um campo existe"""
    field = context.driver.find_element(By.ID, field_id)
    assert field.is_displayed(), f"Campo '{field_id}' não está visível"

@then('deve exibir o botão "{button_text}"')
def step_verify_button_exists(context, button_text):
    """Verifica se um botão existe"""
    button = context.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    assert button.is_displayed(), f"Botão '{button_text}' não está visível"

@then('devo ser redirecionado para o painel do administrador')
def step_verify_admin_dashboard(context):
    """Verifica se foi redirecionado para o painel do admin"""
    time.sleep(3)
    # Verificar URL ou elemento característico do painel
    assert "painel" in context.driver.current_url.lower() or "dashboard" in context.driver.current_url.lower()

@then('devo ser redirecionado para o painel do 2º Grau')
def step_verify_second_degree_dashboard(context):
    """Verifica redirecionamento para 2º Grau"""
    time.sleep(3)
    assert "2g" in context.driver.current_url.lower()

@then('deve exibir mensagem de erro de autenticação')
def step_verify_auth_error(context):
    """Verifica se há mensagem de erro"""
    error = context.driver.find_element(By.XPATH, "//div[@class='error-message' or @class='alert-danger']")
    assert error.is_displayed()

@then('deve exibir mensagem solicitando preenchimento dos campos obrigatórios')
def step_verify_required_fields_message(context):
    """Verifica mensagem de campos obrigatórios"""
    message = context.driver.find_element(By.XPATH, "//*[contains(text(), 'obrigatório')]")
    assert message.is_displayed()

@then('devo visualizar o painel de controle do administrador')
def step_verify_admin_dashboard_content(context):
    """Verifica conteúdo do painel administrativo"""
    dashboard = context.driver.find_element(By.XPATH, "//div[@class='admin-dashboard' or @id='painel']")
    assert dashboard.is_displayed()

@then('devem estar visíveis os widgets disponíveis')
def step_verify_widgets(context):
    """Verifica se widgets estão visíveis"""
    widgets = context.driver.find_elements(By.XPATH, "//div[@class='widget']")
    assert len(widgets) > 0, "Nenhum widget encontrado"

@then('o menu "{menu_name}" deve estar ativo')
def step_verify_menu_active(context, menu_name):
    """Verifica se um menu está ativo"""
    active_menu = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{menu_name}')]/parent::li[@class='active']")
    assert active_menu.is_displayed()

@then('devo visualizar a lista de processos')
def step_verify_process_list(context):
    """Verifica se lista de processos está visível"""
    process_list = context.driver.find_element(By.XPATH, "//table[@class='process-list' or @id='processos-table']")
    assert process_list.is_displayed()

@then('devem estar disponíveis os filtros de busca')
def step_verify_search_filters(context):
    """Verifica se filtros de busca estão disponíveis"""
    filters = context.driver.find_elements(By.XPATH, "//div[@class='filter-panel']//input")
    assert len(filters) > 0, "Nenhum filtro encontrado"

# =============================================================================
# Hooks - Antes e Depois de cada cenário
# =============================================================================

def after_scenario(context, scenario):
    """Limpa recursos após cada cenário"""
    if hasattr(context, 'driver'):
        context.driver.quit()
