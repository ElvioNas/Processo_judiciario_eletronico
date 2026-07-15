# Guia de Testes Gherkin - PJe 1º e 2º Grau

## 📋 Visão Geral

Este projeto utiliza **Gherkin** e **Behave** para descrever cenários de teste em linguagem natural (português), facilitando a colaboração entre desenvolvedores, QA e stakeholders.

## 📁 Estrutura de Diretórios

```
1ºGrau/
├── features/
│   ├── telaPrincipal.feature          # Validação da tela inicial
│   ├── autenticacao.feature           # Testes de login e autenticação
│   ├── menuNavigacao.feature          # Navegação entre menus
│   ├── papeisPermissoes.feature       # Diferentes perfis de usuário
│   ├── fluxoGestaoProcessos.feature   # Fluxo completo de processos
│   └── steps.py                        # Implementação dos passos

2ºGrau/
├── features/
│   ├── telaPrincipal.feature
│   └── steps.py                        # Passos compartilhados/específicos
```

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)
- Chrome/Chromium instalado

### Instalação de Dependências

```bash
# Instalar Behave (framework BDD)
pip install behave

# Instalar Selenium
pip install selenium

# Instalar ChromeDriver (ou use uma versão compatível com seu Chrome)
pip install webdriver-manager
```

## 📝 Estrutura de um Arquivo .feature

```gherkin
# language: pt
Funcionalidade: Descrição da funcionalidade

  Contexto:
    Dado que <pré-condição 1>
    E <pré-condição 2>

  Cenário: Descrição do cenário 1
    Quando <ação 1>
    E <ação 2>
    Então <validação 1>
    E <validação 2>

  Cenário: Descrição do cenário 2
    Quando <ação>
    Então <validação>
```

### Palavras-chave
- **Funcionalidade**: Agrupa cenários relacionados
- **Contexto**: Pré-condições comuns a todos os cenários
- **Cenário**: Um teste específico
- **Dado/Dado que**: Pré-condições (Given)
- **Quando**: Ações do usuário (When)
- **Então**: Validações esperadas (Then)
- **E**: Conecta múltiplas etapas
- **Mas**: Alternativa negativa

## 🏃 Execução dos Testes

### Executar todos os testes de 1º Grau
```bash
cd 1ºGrau
behave
```

### Executar uma feature específica
```bash
behave features/telaPrincipal.feature
```

### Executar um cenário específico
```bash
behave features/autenticacao.feature:15
```

### Executar com relatório
```bash
behave --format html --outfile report.html
```

### Executar com tag
```bash
# Adicionar tags nos cenários:
# @smoke
# Cenário: ...

behave --tags=@smoke
```

## 📊 Relatórios

Behave gera relatórios automaticamente:

```bash
# Formato padrão
behave --format pretty

# Formato HTML
behave --format html --outfile report.html

# Formato JSON
behave --format json --outfile report.json
```

## 🔐 Gerenciamento de Credenciais

**IMPORTANTE**: Nunca commitar credenciais no código!

### Usando variáveis de ambiente

```python
import os

@given('realizo login com as credenciais de administrador')
def step_login_admin(context):
    username = os.getenv('PJE_ADMIN_USER', '02112357417')
    password = os.getenv('PJE_ADMIN_PASS', 'tjpe1977')
    
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "btnEntrar").click()
```

### Arquivo de configuração `.env`

```bash
# .env (não commitar este arquivo!)
PJE_ADMIN_USER=02112357417
PJE_ADMIN_PASS=tjpe1977
PJE_LAWYER_USER=...
PJE_LAWYER_PASS=...
```

Instalar biblioteca para carregar .env:
```bash
pip install python-dotenv
```

## 📋 Features Disponíveis

### 1. **telaPrincipal.feature**
- ✅ Validação de títulos e labels
- ✅ Verificação de links de acesso
- ✅ Disponibilidade de campos de login

### 2. **autenticacao.feature**
- ✅ Login com credenciais válidas
- ✅ Tentativa com credenciais inválidas
- ✅ Campos vazios
- ✅ Recuperação de senha

### 3. **menuNavigacao.feature**
- ✅ Acesso a cada menu
- ✅ Validação de conteúdo de cada menu
- ✅ Navegação entre menus
- ✅ Estados de ativação de menu

### 4. **papeisPermissoes.feature**
- ✅ Validação de permissões por papel (administrador, advogado, magistrado, promotor, oficial de justiça)
- ✅ Acesso/restrição a funcionalidades específicas

### 5. **fluxoGestaoProcessos.feature**
- ✅ Fluxo completo de consulta de processo
- ✅ Gerenciamento de atividades
- ✅ Agendamento de audiência
- ✅ Download de documentos

## 📐 Melhores Práticas

### 1. Mantenha Cenários Independentes
Cada cenário deve ser capaz de rodar isoladamente.

### 2. Use Contexto Compartilhado
```gherkin
Contexto:
  Dado que o navegador está aberto
  E que estou logado
```

### 3. Evite Detalhes Técnicos
Gherkin é para negócio/QA, não para técnicos:

❌ Ruim:
```gherkin
Quando seleciono o elemento com XPath "//div[@class='btn-submit']"
```

✅ Bom:
```gherkin
Quando clico no botão "Enviar"
```

### 4. Use Tabelas para Múltiplos Dados
```gherkin
Quando preencho o formulário com:
  | Campo    | Valor       |
  | Nome     | João Silva  |
  | Email    | joao@test   |
  | Telefone | 1234567890  |
```

### 5. Reutilize Steps
Implemente steps de forma genérica para máxima reutilização.

## 🔍 Troubleshooting

### Erro: ChromeDriver not found
```bash
pip install webdriver-manager
```

### Erro: Element not found
- Verifique os XPath/ID/CSS Selectors
- Adicione waits adequados
- Use `time.sleep()` ou Explicit Waits

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.ID, "meuElemento"))
)
```

### Erro: Behave command not found
```bash
# Instalar novamente
pip install --upgrade behave

# Ou executar com módulo Python
python -m behave
```

## 📚 Recursos Adicionais

- [Documentação Behave](https://behave.readthedocs.io/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/reference/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)

## 👥 Contribuição

1. Crie um branch para sua feature
2. Adicione novos cenários em `.feature`
3. Implemente os steps em `steps.py`
4. Execute `behave` para validar
5. Faça Pull Request

## 📞 Suporte

Para dúvidas sobre Gherkin/BDD/Behave, consulte:
- A equipe de QA
- Documentação oficial do Behave
- Exemplos neste repositório

---

**Última atualização**: 15/07/2026
