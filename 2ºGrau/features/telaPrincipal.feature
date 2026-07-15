# language: pt
Funcionalidade: Validação da Tela Principal do PJe 2º Grau

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam"
    E aguardar 2 segundos para carregar a página

  Cenário: Validar exibição de títulos na tela principal 2º Grau
    Então deve exibir o título "Processo Judicial Eletrônico"
    E deve exibir o subtítulo "Processo Judicial Eletrônico 2º Grau"
    E deve exibir "Poder Judiciário de Pernambuco"

  Cenário: Validar exibição de links de acesso do 2º Grau
    Então deve exibir o link "Formas de acesso"
    E deve exibir o link "Consulta processual"
    E deve exibir o link "Push"
    E deve exibir o link "Manuais"
    E deve exibir o link "Fale conosco"

  Cenário: Validar links específicos do 2º Grau
    Então deve exibir o link "Solicitar nova senha"
    E deve exibir o link "Saiba como obter o certificado digital"

  Cenário: Validar campo de login
    Então deve exibir o campo de entrada para "username"
    E deve exibir o campo de entrada para "password"
    E deve exibir o botão "Entrar"
