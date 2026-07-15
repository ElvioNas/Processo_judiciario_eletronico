# language: pt
Funcionalidade: Autenticação no PJe 2º Grau

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam"
    E aguardar 2 segundos para carregar a página

  Cenário: Login com credenciais válidas de administrador do 2º Grau
    Quando preencho o campo "username" com "02112357417"
    E aguardo 2 segundos
    E preencho o campo "password" com "123"
    E aguardo 2 segundos
    E clico no botão "btnEntrar"
    E aguardo 3 segundos
    Então devo ser redirecionado para o painel do 2º Grau

  Cenário: Tentativa de login com usuário inválido no 2º Grau
    Quando preencho o campo "username" com "00000000000"
    E aguardo 1 segundo
    E preencho o campo "password" com "senhaerrada"
    E aguardo 1 segundo
    E clico no botão "btnEntrar"
    Então deve exibir mensagem de erro de autenticação

  Cenário: Tentativa de login com campos vazios no 2º Grau
    Quando clico no botão "btnEntrar"
    Então deve exibir mensagem solicitando preenchimento dos campos obrigatórios

  Cenário: Recuperação de senha no 2º Grau
    Quando clico no link "Solicitar nova senha"
    Então devo ser redirecionado para a página de recuperação de senha

  Cenário: Acesso à informação de certificado digital
    Quando clico no link "Saiba como obter o certificado digital"
    Então devo visualizar a página de informações sobre certificado digital
