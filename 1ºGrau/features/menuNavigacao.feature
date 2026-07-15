# language: pt
Funcionalidade: Navegação de Menus do PJe 1º Grau - Administrador

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam"
    E realizo login com as credenciais de administrador
    E aguardo a página principal carregar completamente

  Cenário: Acessar Menu 1 - Painel
    Quando clico no menu "Painel"
    Então devo visualizar o painel de controle do administrador
    E devem estar visíveis os widgets disponíveis
    E o menu "Painel" deve estar ativo

  Cenário: Acessar Menu 2 - Processos
    Quando clico no menu "Processos"
    Então devo visualizar a lista de processos
    E devem estar disponíveis os filtros de busca
    E o menu "Processos" deve estar ativo

  Cenário: Acessar Menu 3 - Atividades
    Quando clico no menu "Atividades"
    Então devo visualizar as atividades pendentes
    E devem estar listadas as atividades por prioridade
    E o menu "Atividades" deve estar ativo

  Cenário: Acessar Menu 4 - Audiências e Sessões
    Quando clico no menu "Audiências e Sessões"
    Então devo visualizar o calendário de audiências
    E devem estar listadas as sessões agendadas
    E o menu "Audiências e Sessões" deve estar ativo

  Cenário: Acessar Menu 5 - Configurações
    Quando clico no menu "Configurações"
    Então devo visualizar as opções de configuração do sistema
    E devem estar disponíveis as configurações administrativas
    E o menu "Configurações" deve estar ativo

  Cenário: Acessar Menu 6 - Download
    Quando clico no menu "Download"
    Então devo visualizar a área de downloads
    E devem estar listados os arquivos disponíveis para download
    E o menu "Download" deve estar ativo

  Cenário: Navegar entre menus
    Quando clico no menu "Processos"
    E aguardo 1 segundo
    E clico no menu "Atividades"
    Então o menu "Atividades" deve estar ativo
    E o menu "Processos" deve estar inativo
