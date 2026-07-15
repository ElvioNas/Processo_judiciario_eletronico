# language: pt
Funcionalidade: Validação de Papéis e Permissões no PJe 1º Grau

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam"

  Cenário: Administrador acessa todos os menus
    Quando realizo login com credenciais de administrador
    Então devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download
    E devo ter acesso a todas as funcionalidades administrativas

  Cenário: Advogado visualiza menus permitidos
    Quando realizo login com credenciais de advogado
    Então devo visualizar os menus: Painel, Processos, Atividades, Configurações, Download
    E não devo ter acesso ao menu "Audiências e Sessões"
    E não devo ter acesso a funcionalidades administrativas

  Cenário: Magistrado acessa funcionalidades de magistrado
    Quando realizo login com credenciais de magistrado
    Então devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download
    E devo ter acesso a funcionalidades de sessões judiciais

  Cenário: Promotor acessa funcionalidades de promotor
    Quando realizo login com credenciais de promotor
    Então devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download
    E devo ter acesso a funcionalidades de órgão ministerial

  Cenário: Oficial de Justiça visualiza menus permitidos
    Quando realizo login com credenciais de oficial de justiça
    Então devo visualizar os menus: Painel, Processos, Atividades, Configurações, Download
    E não devo ter acesso ao menu "Audiências e Sessões"
    E devo ter acesso apenas a funcionalidades de distribuição de atos processuais
