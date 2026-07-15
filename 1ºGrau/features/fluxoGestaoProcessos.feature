# language: pt
Funcionalidade: Fluxo Completo de Gestão de Processos - 1º Grau

  Contexto:
    Dado que o navegador está aberto maximizado
    E que acesso a URL da tela inicial "https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam"
    E realizo login como administrador
    E aguardo a página principal carregar completamente

  Cenário: Fluxo completo de consulta e manipulação de processo
    Quando clico no menu "Processos"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar a lista de processos disponíveis
    
    Quando preencho o campo de busca com "0000001-86.2023.7.05.0001"
    E pressiono Enter
    E aguardo 2 segundos para o resultado carregar
    Então devo visualizar o processo na lista

    Quando clico no processo encontrado
    E aguardo 2 segundos para a página de detalhe carregar
    Então devo visualizar os detalhes do processo
    E devo visualizar o número do processo
    E devo visualizar as partes envolvidas
    E devo visualizar o histórico de movimentações

  Cenário: Gerenciamento de atividades
    Quando clico no menu "Atividades"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar a lista de atividades pendentes
    
    Quando seleciono a primeira atividade da lista
    Então devo visualizar os detalhes da atividade
    E devo visualizar o prazo da atividade
    
    Quando clico no botão "Concluir"
    Então a atividade deve ser marcada como concluída
    E devo visualizar uma mensagem de sucesso

  Cenário: Agendamento de audiência
    Quando clico no menu "Audiências e Sessões"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar o calendário de audiências
    
    Quando clico no botão "Agendar Nova Audiência"
    E preencho o formulário de agendamento:
      | Campo               | Valor                        |
      | Tipo de Audiência   | Instrução e Julgamento      |
      | Data                | 25/12/2024                  |
      | Hora                | 14:00                       |
      | Local               | Sala 01 - 1º Andar          |
      | Juiz Relator        | Des. João da Silva          |
    E clico no botão "Salvar"
    Então devo visualizar uma mensagem de sucesso
    E a audiência deve aparecer no calendário

  Cenário: Download de documentos
    Quando clico no menu "Download"
    E aguardo 2 segundos para a página carregar
    Então devo visualizar a lista de documentos disponíveis
    
    Quando seleciono o documento "Decisão - Processo 0000001-86.2023.7.05.0001"
    E clico no botão "Download"
    Então o arquivo deve ser baixado com sucesso
    E o nome do arquivo deve ser válido
