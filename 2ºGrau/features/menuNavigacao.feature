# language: pt
Funcionalidade: Navegação de Menus do PJe 2º Grau - Administrador

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam"
    E realizo login com as credenciais de administrador do 2º Grau
    E aguardo a página principal carregar completamente

  Cenário: Acessar Menu 1 - Painel do 2º Grau
    Quando clico no menu "Painel"
    Então devo visualizar o painel de controle do administrador
    E devem estar visíveis os widgets disponíveis
    E o menu "Painel" deve estar ativo

  Cenário: Acessar Menu 2 - Processos do 2º Grau
    Quando clico no menu "Processos"
    Então devo visualizar a lista de processos do 2º Grau
    E devem estar disponíveis os filtros de busca
    E o menu "Processos" deve estar ativo

  Cenário: Acessar Menu 3 - Atividades do 2º Grau
    Quando clico no menu "Atividades"
    Então devo visualizar as atividades pendentes
    E devem estar listadas as atividades por prioridade
    E o menu "Atividades" deve estar ativo

  Cenário: Acessar Menu 4 - Audiências e Sessões do 2º Grau
    Quando clico no menu "Audiências e Sessões"
    Então devo visualizar o calendário de audiências do 2º Grau
    E devem estar listadas as sessões agendadas
    E o menu "Audiências e Sessões" deve estar ativo

  Cenário: Acessar Menu 5 - Configurações do 2º Grau
    Quando clico no menu "Configurações"
    Então devo visualizar as opções de configuração do sistema
    E devem estar disponíveis as configurações administrativas do 2º Grau
    E o menu "Configurações" deve estar ativo

  Cenário: Acessar Menu 6 - Download do 2º Grau
    Quando clico no menu "Download"
    Então devo visualizar a área de downloads
    E devem estar listados os arquivos disponíveis para download
    E o menu "Download" deve estar ativo

  Cenário: Navegar entre menus do 2º Grau
    Quando clico no menu "Processos"
    E aguardo 1 segundo
    E clico no menu "Atividades"
    Então o menu "Atividades" deve estar ativo
    E o menu "Processos" deve estar inativo
