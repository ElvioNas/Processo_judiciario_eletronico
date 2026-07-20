#language: pt

Funcionalidade: Painel do Representante Processual - Expediente
  Como um administrador do PJe
  Eu quero acessar o painel do representante processual
  Para visualizar e gerenciar expedientes com diferentes status

  Contexto:
    Dado que o sistema PJe 1º Grau está disponível
    E eu estou na tela principal de login

  Cenário: Acessar o painel do representante processual com sucesso
    Quando eu faço login com usuário "02112357417" e senha "tjpe1977"
    E eu clico no menu principal
    E eu seleciono a opção "Painel"
    E eu clico em "Painel do representante processual"
    Então eu devo ver a seção de "Expedientes"

  Cenário: Validar filtros de expediente disponíveis
    Quando eu faço login com usuário "02112357417" e senha "tjpe1977"
    E eu clico no menu principal
    E eu seleciono a opção "Painel"
    E eu clico em "Painel do representante processual"
    Então eu devo visualizar os seguintes filtros de expediente:
      | Filtro                                                                 |
      | Pendentes de ciência ou de resposta                                   |
      | Apenas pendentes de ciência                                           |
      | Ciência dada pelo destinatário direto ou indireto - pendente de resposta |
      | Ciência dada pelo Judiciário - pendente de resposta                    |
      | Cujo prazo findou nos últimos 10 dias - sem resposta                   |
      | Sem prazo                                                             |
      | Respondidos nos últimos 10 dias                                       |

  Cenário: Validar campo "Expedientes" no painel do representante processual
    Quando eu faço login com usuário "02112357417" e senha "tjpe1977"
    E eu clico no menu principal
    E eu seleciono a opção "Painel"
    E eu clico em "Painel do representante processual"
    Então o campo de "Expedientes" deve estar visível na tela
