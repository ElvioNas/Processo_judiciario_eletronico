# language: pt
Funcionalidade: Fluxo Completo de Gestão de Processos - 2º Grau

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam"
    E realizo login como administrador do 2º Grau
    E aguardo a página principal carregar completamente

  Cenário: Fluxo completo de consulta e manipulação de processo no 2º Grau
    Quando clico no menu "Processos"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar a lista de processos do 2º Grau
    
    Quando preencho o campo de busca com "0000001-86.2023.8.05.0000"
    E pressiono Enter
    E aguardo 2 segundos para o resultado carregar
    Então devo visualizar o processo na lista

    Quando clico no processo encontrado
    E aguardo 2 segundos para a página de detalhe carregar
    Então devo visualizar os detalhes do processo do 2º Grau
    E devo visualizar o número do processo
    E devo visualizar as partes envolvidas
    E devo visualizar o histórico de movimentações

  Cenário: Gerenciamento de atividades do 2º Grau
    Quando clico no menu "Atividades"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar a lista de atividades pendentes
    
    Quando seleciono a primeira atividade da lista
    Então devo visualizar os detalhes da atividade
    E devo visualizar o prazo da atividade
    
    Quando clico no botão "Concluir"
    Então a atividade deve ser marcada como concluída
    E devo visualizar uma mensagem de sucesso

  Cenário: Agendamento de sessão no 2º Grau
    Quando clico no menu "Audiências e Sessões"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar o calendário de sessões do 2º Grau
    
    Quando clico no botão "Agendar Nova Sessão"
    E preencho o formulário de agendamento:
      | Campo               | Valor                        |
      | Tipo de Sessão      | Julgamento de Apelação       |
      | Data                | 25/12/2024                  |
      | Hora                | 14:00                       |
      | Local               | Plenário - 2º Andar         |
      | Desembargador       | Des. Maria da Silva         |
    E clico no botão "Salvar"
    Então devo visualizar uma mensagem de sucesso
    E a sessão deve aparecer no calendário

  Cenário: Download de acórdãos e decisões
    Quando clico no menu "Download"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar a lista de documentos disponíveis
    
    Quando seleciono o documento "Acórdão - Processo 0000001-86.2023.8.05.0000"
    E clico no botão "Download"
    Então o arquivo deve ser baixado com sucesso
    E o nome do arquivo deve ser válido

  Cenário: Consulta de jurisprudência
    Quando clico no menu "Processos"
    E aguardo 2 segundos para a página carregar
    E clico no link "Jurisprudência"
    Então devo visualizar a base de jurisprudência
    E devo poder buscar decisões e acórdãos anteriores
    E devo visualizar as referências dos precedentes
