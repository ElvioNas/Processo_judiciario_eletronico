# language: pt
Funcionalidade: Validação de Papéis e Permissões no PJe 2º Grau

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam"

  Cenário: Administrador acessa todos os menus do 2º Grau
    Quando realizo login com credenciais de administrador do 2º Grau
    Então devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download
    E devo ter acesso a todas as funcionalidades administrativas do 2º Grau

  Cenário: Advogado visualiza menus permitidos no 2º Grau
    Quando realizo login com credenciais de advogado do 2º Grau
    Então devo visualizar os menus: Painel, Processos, Atividades, Configurações, Download
    E não devo ter acesso ao menu "Audiências e Sessões"
    E não devo ter acesso a funcionalidades administrativas

  Cenário: Magistrado acessa funcionalidades de magistrado no 2º Grau
    Quando realizo login com credenciais de magistrado do 2º Grau
    Então devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download
    E devo ter acesso a funcionalidades de sessões judiciais do 2º Grau

  Cenário: Promotor acessa funcionalidades de promotor no 2º Grau
    Quando realizo login com credenciais de promotor do 2º Grau
    Então devo visualizar os menus: Painel, Processos, Atividades, Audiências e Sessões, Configurações, Download
    E devo ter acesso a funcionalidades de órgão ministerial do 2º Grau

  Cenário: Oficial de Justiça visualiza menus permitidos no 2º Grau
    Quando realizo login com credenciais de oficial de justiça do 2º Grau
    Então devo visualizar os menus: Painel, Processos, Atividades, Configurações, Download
    E não devo ter acesso ao menu "Audiências e Sessões"
    E devo ter acesso apenas a funcionalidades de distribuição de atos processuais
