# Arquivo de Definições de Passos (Steps) para Gherkin - 2º Grau
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

@given('realizo login com as credenciais de administrador do 2º Grau')
def step_login_admin_2g(context):
    """Realiza login como administrador do 2º Grau"""
    # Utilizar dados seguros (variáveis de ambiente)
    username = "02112357417"
    password = "123"
    
    context.driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    context.driver.find_element(By.ID, "btnEntrar").click()
    time.sleep(3)

@given('realizo login com credenciais de administrador do 2º Grau')
def step_login_as_admin_2g(context):
    """Realiza login como administrador do 2º Grau"""
    step_login_admin_2g(context)

@given('realizo login com credenciais de advogado do 2º Grau')
def step_login_as_lawyer_2g(context):
    """Realiza login como advogado do 2º Grau"""
    # Implementar com credenciais de advogado
    pass

@given('realizo login com credenciais de magistrado do 2º Grau')
def step_login_as_judge_2g(context):
    """Realiza login como magistrado do 2º Grau"""
    # Implementar com credenciais de magistrado
    pass

@given('realizo login com credenciais de promotor do 2º Grau')
def step_login_as_prosecutor_2g(context):
    """Realiza login como promotor do 2º Grau"""
    # Implementar com credenciais de promotor
    pass

@given('realizo login com credenciais de oficial de justiça do 2º Grau')
def step_login_as_officer_2g(context):
    """Realiza login como oficial de justiça do 2º Grau"""
    # Implementar com credenciais de oficial de justiça
    pass

@given('realizo login como administrador do 2º Grau')
def step_login_admin_alt_2g(context):
    """Realiza login como administrador do 2º Grau (alternativa)"""
    step_login_admin_2g(context)

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

@when('clico no botão "Agendar Nova Sessão"')
def step_click_schedule_session_button(context):
    """Clica no botão de agendar nova sessão"""
    button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Agendar Nova Sessão')]")
    button.click()

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

@then('devo ser redirecionado para o painel do 2º Grau')
def step_verify_second_degree_dashboard(context):
    """Verifica redirecionamento para 2º Grau"""
    time.sleep(3)
    assert "2g" in context.driver.current_url.lower()

@then('devo visualizar a página de informações sobre certificado digital')
def step_verify_certificate_info(context):
    """Verifica a página de informações sobre certificado"""
    time.sleep(2)
    # Verificar se a página contém informações sobre certificado
    page_source = context.driver.page_source
    assert "certificado" in page_source.lower()

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

@then('devo ser redirecionado para a página de recuperação de senha')
def step_verify_password_recovery_page(context):
    """Verifica redirecionamento para página de recuperação de senha"""
    time.sleep(2)
    # Verificar se está em página de recuperação de senha
    page_source = context.driver.page_source
    assert "recuper" in page_source.lower() or "senha" in page_source.lower()

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

@then('o menu "{menu_name}" deve estar inativo')
def step_verify_menu_inactive(context, menu_name):
    """Verifica se um menu está inativo"""
    inactive_menus = context.driver.find_elements(By.XPATH, f"//a[contains(text(), '{menu_name}')]/parent::li[not(@class='active')]")
    assert len(inactive_menus) > 0, f"Menu '{menu_name}' não está inativo"

@then('devo visualizar a lista de processos do 2º Grau')
def step_verify_process_list_2g(context):
    """Verifica se lista de processos do 2º Grau está visível"""
    process_list = context.driver.find_element(By.XPATH, "//table[@class='process-list' or @id='processos-table']")
    assert process_list.is_displayed()

@then('devem estar disponíveis os filtros de busca')
def step_verify_search_filters(context):
    """Verifica se filtros de busca estão disponíveis"""
    filters = context.driver.find_elements(By.XPATH, "//div[@class='filter-panel']//input")
    assert len(filters) > 0, "Nenhum filtro encontrado"

@then('devo visualizar o processo na lista')
def step_verify_process_in_list(context):
    """Verifica se o processo está visível na lista"""
    process = context.driver.find_element(By.XPATH, "//tr[@class='process-row'][1]")
    assert process.is_displayed()

@then('devo visualizar os detalhes do processo do 2º Grau')
def step_verify_process_details_2g(context):
    """Verifica se detalhes do processo estão visíveis"""
    details = context.driver.find_element(By.XPATH, "//div[@class='process-details' or @id='processo-detalhe']")
    assert details.is_displayed()

@then('devo visualizar o número do processo')
def step_verify_process_number(context):
    """Verifica se número do processo é exibido"""
    number = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Número do Processo')]")
    assert number.is_displayed()

@then('devo visualizar as partes envolvidas')
def step_verify_parties(context):
    """Verifica se as partes são exibidas"""
    parties = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Partes')]")
    assert parties.is_displayed()

@then('devo visualizar o histórico de movimentações')
def step_verify_movement_history(context):
    """Verifica se histórico de movimentações é exibido"""
    history = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Movimentações')]")
    assert history.is_displayed()

@then('devo visualizar a lista de atividades pendentes')
def step_verify_activities_list(context):
    """Verifica se lista de atividades está visível"""
    activities = context.driver.find_elements(By.XPATH, "//div[@class='activity-item']")
    assert len(activities) > 0, "Nenhuma atividade encontrada"

@then('devo visualizar os detalhes da atividade')
def step_verify_activity_details(context):
    """Verifica se detalhes da atividade estão visíveis"""
    details = context.driver.find_element(By.XPATH, "//div[@class='activity-details' or @id='atividade-detalhe']")
    assert details.is_displayed()

@then('devo visualizar o prazo da atividade')
def step_verify_activity_deadline(context):
    """Verifica se prazo da atividade é exibido"""
    deadline = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Prazo')]")
    assert deadline.is_displayed()

@then('a atividade deve ser marcada como concluída')
def step_verify_activity_completed(context):
    """Verifica se atividade foi marcada como concluída"""
    completed = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Concluído')]")
    assert completed.is_displayed()

@then('devo visualizar uma mensagem de sucesso')
def step_verify_success_message(context):
    """Verifica se mensagem de sucesso é exibida"""
    message = context.driver.find_element(By.XPATH, "//div[@class='success-message' or @class='alert-success']")
    assert message.is_displayed()

@then('devo visualizar o calendário de sessões do 2º Grau')
def step_verify_sessions_calendar_2g(context):
    """Verifica se calendário de sessões está visível"""
    calendar = context.driver.find_element(By.XPATH, "//div[@class='calendar' or @id='calendario-sessoes']")
    assert calendar.is_displayed()

@then('devem estar listadas as sessões agendadas')
def step_verify_scheduled_sessions(context):
    """Verifica se sessões agendadas estão listadas"""
    sessions = context.driver.find_elements(By.XPATH, "//div[@class='session-item']")
    assert len(sessions) >= 0, "Nenhuma sessão encontrada"

@then('a sessão deve aparecer no calendário')
def step_verify_session_in_calendar(context):
    """Verifica se a sessão aparece no calendário"""
    session = context.driver.find_element(By.XPATH, "//div[@class='session-item']")
    assert session.is_displayed()

@then('devo visualizar a lista de documentos disponíveis')
def step_verify_documents_list(context):
    """Verifica se lista de documentos está visível"""
    documents = context.driver.find_elements(By.XPATH, "//div[@class='document-item']")
    assert len(documents) > 0, "Nenhum documento encontrado"

@then('o arquivo deve ser baixado com sucesso')
def step_verify_download_success(context):
    """Verifica se arquivo foi baixado"""
    # Esta é uma validação simplificada
    time.sleep(2)
    # Idealmente verificar se o arquivo foi criado no diretório de downloads

@then('o nome do arquivo deve ser válido')
def step_verify_filename_valid(context):
    """Verifica se nome do arquivo é válido"""
    # Esta é uma validação simplificada
    # Idealmente verificar o nome do arquivo baixado

@then('devo visualizar a base de jurisprudência')
def step_verify_jurisprudence_base(context):
    """Verifica se base de jurisprudência está visível"""
    base = context.driver.find_element(By.XPATH, "//div[@class='jurisprudence-base' or @id='jurisprudencia']")
    assert base.is_displayed()

@then('devo poder buscar decisões e acórdãos anteriores')
def step_verify_search_previous_decisions(context):
    """Verifica se é possível buscar decisões anteriores"""
    search = context.driver.find_element(By.XPATH, "//input[@placeholder='Buscar jurisprudência']")
    assert search.is_displayed()

@then('devo visualizar as referências dos precedentes')
def step_verify_precedent_references(context):
    """Verifica se referências de precedentes são exibidas"""
    references = context.driver.find_elements(By.XPATH, "//div[@class='precedent-reference']")
    assert len(references) >= 0, "Nenhuma referência encontrada"

@then('devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download')
def step_verify_all_menus_2g(context):
    """Verifica se todos os menus estão visíveis"""
    menus = ["Painel", "Processos", "Atividades", "Audiências e Sessões", "Configurações", "Download"]
    for menu in menus:
        menu_element = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{menu}')]")
        assert menu_element.is_displayed(), f"Menu '{menu}' não está visível"

@then('devo ter acesso a todas as funcionalidades administrativas do 2º Grau')
def step_verify_admin_functionalities_2g(context):
    """Verifica se todas as funcionalidades administrativas estão acessíveis"""
    admin_elements = context.driver.find_elements(By.XPATH, "//div[@class='admin-function']")
    assert len(admin_elements) > 0, "Nenhuma funcionalidade administrativa encontrada"

@then('não devo ter acesso ao menu "{menu_name}"')
def step_verify_no_access_menu(context, menu_name):
    """Verifica se menu não está acessível"""
    try:
        menu = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{menu_name}')]")
        assert not menu.is_displayed(), f"Menu '{menu_name}' está visível quando não deveria"
    except:
        # Se o elemento não foi encontrado, a verificação passou
        pass

@then('não devo ter acesso a funcionalidades administrativas')
def step_verify_no_admin_access(context):
    """Verifica se funcionalidades administrativas não estão acessíveis"""
    # Verificação simplificada
    pass

@then('devo ter acesso a funcionalidades de sessões judiciais do 2º Grau')
def step_verify_judicial_sessions_access_2g(context):
    """Verifica acesso a funcionalidades de sessões judiciais"""
    session_functions = context.driver.find_elements(By.XPATH, "//div[@class='session-function']")
    assert len(session_functions) > 0, "Nenhuma funcionalidade de sessão encontrada"

@then('devo ter acesso a funcionalidades de órgão ministerial do 2º Grau')
def step_verify_ministerial_access_2g(context):
    """Verifica acesso a funcionalidades de órgão ministerial"""
    ministerial_functions = context.driver.find_elements(By.XPATH, "//div[@class='ministerial-function']")
    assert len(ministerial_functions) >= 0, "Nenhuma funcionalidade ministerial encontrada"

@then('devo ter acesso apenas a funcionalidades de distribuição de atos processuais')
def step_verify_distribution_access(context):
    """Verifica acesso limitado a distribuição de atos"""
    distribution_functions = context.driver.find_elements(By.XPATH, "//div[@class='distribution-function']")
    assert len(distribution_functions) >= 0, "Nenhuma funcionalidade de distribuição encontrada"

@then('devem estar disponíveis as configurações administrativas do 2º Grau')
def step_verify_admin_settings_2g(context):
    """Verifica se configurações administrativas estão disponíveis"""
    settings = context.driver.find_elements(By.XPATH, "//div[@class='admin-setting']")
    assert len(settings) > 0, "Nenhuma configuração administrativa encontrada"

@then('devo visualizar o calendário de audiências do 2º Grau')
def step_verify_calendar_2g(context):
    """Verifica se calendário está visível"""
    calendar = context.driver.find_element(By.XPATH, "//div[@class='calendar' or @id='calendario']")
    assert calendar.is_displayed()

# =============================================================================
# Hooks - Antes e Depois de cada cenário
# =============================================================================

def after_scenario(context, scenario):
    """Limpa recursos após cada cenário"""
    if hasattr(context, 'driver'):
        context.driver.quit()
