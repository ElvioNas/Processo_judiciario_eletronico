# Guia de Testes Gherkin - PJe 2º Grau

## 📋 Visão Geral

Este diretório contém os cenários Gherkin específicos para o **PJe 2º Grau**, incluindo testes para todas as funcionalidades do segundo grau do Poder Judiciário.

## 📁 Estrutura de Diretórios

```
2ºGrau/
├── features/
│   ├── telaPrincipal.feature          # Validação da tela inicial 2º Grau
│   ├── autenticacao.feature           # Testes de login (senha: 123)
│   ├── menuNavigacao.feature          # Navegação entre menus
│   ├── papeisPermissoes.feature       # Diferentes perfis de usuário
│   ├── fluxoGestaoProcessos.feature   # Fluxo completo de processos do 2º Grau
│   ├── steps.py                        # Implementação dos passos (2º Grau)
│   └── environment.py                  # Setup/Teardown (2º Grau)
```

## 🔑 Diferenças entre 1º Grau e 2º Grau

### URL Base
- **1º Grau**: `https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam`
- **2º Grau**: `https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam`

### Credenciais
- **Usuário**: `02112357417` (igual em ambos)
- **Senha 1º Grau**: `tjpe1977`
- **Senha 2º Grau**: `123`

### Elementos Específicos 2º Grau
- Link adicional: "Saiba como obter o certificado digital"
- Subtítulo: "Processo Judicial Eletrônico 2º Grau"

### Funcionalidades Específicas
- **Processosː**: Gerenciamento de apelações e recursos
- **Sessionasː**: Julgamentos de apelação em Plenário
- **Documentosː**: Acórdãos e decisões de segunda instância
- **Jurisprudênciaː**: Busca de precedentes e jurisprudência consolidada

## 🚀 Instalação

Consulte o `README_GHERKIN.md` no diretório raiz para instruções completas.

```bash
pip install behave selenium webdriver-manager
```

## 📝 Execução dos Testes

### Executar todos os testes do 2º Grau
```bash
cd 2ºGrau
behave
```

### Executar uma feature específica
```bash
behave features/autenticacao.feature
```

### Executar com relatório HTML
```bash
behave --format html --outfile report.html
```

### Executar apenas testes de smoke
```bash
# Adicionar @smoke aos cenários que deseja
behave --tags=@smoke
```

## 📊 Features Disponíveis

### 1. **telaPrincipal.feature** (4 cenários)
- ✅ Validação de títulos e labels do 2º Grau
- ✅ Verificação de links de acesso
- ✅ Link adicional de certificado digital
- ✅ Campos de login

### 2. **autenticacao.feature** (5 cenários)
- ✅ Login com credenciais válidas (senha: `123`)
- ✅ Tentativa com credenciais inválidas
- ✅ Campos vazios
- ✅ Recuperação de senha
- ✅ Informações sobre certificado digital

### 3. **menuNavigacao.feature** (7 cenários)
- ✅ Acesso a cada menu
- ✅ Validação de conteúdo específico 2º Grau
- ✅ Navegação entre menus
- ✅ Estados de ativação de menu

### 4. **papeisPermissoes.feature** (5 cenários)
- ✅ Validação de permissões por papel (administrador, advogado, magistrado, promotor, oficial de justiça)
- ✅ Acesso/restrição a funcionalidades específicas 2º Grau

### 5. **fluxoGestaoProcessos.feature** (5 cenários)
- ✅ Fluxo completo de consulta de processo (apelações)
- ✅ Gerenciamento de atividades
- ✅ Agendamento de sessão de julgamento
- ✅ Download de acórdãos
- ✅ Consulta de jurisprudência

## 🔐 Gerenciamento de Credenciais

**IMPORTANTE**: Use variáveis de ambiente para credenciais!

```python
# Exemplo em steps.py
import os

username = os.getenv('PJE_ADMIN_USER', '02112357417')
password = os.getenv('PJE_ADMIN_2G_PASS', '123')
```

### Arquivo .env
```bash
PJE_ADMIN_USER=02112357417
PJE_ADMIN_2G_PASS=123
PJE_LAWYER_2G_USER=...
PJE_LAWYER_2G_PASS=...
```

## 📋 Cenários Inclusos

✅ **26 cenários** cobrindo:
- Validação de elementos da tela principal
- Login com credenciais válidas/inválidas
- Navegação entre menus
- Fluxos completos (processos, atividades, sessões, downloads)
- Permissões por papel (5 papéis diferentes)
- Funcionalidades específicas do 2º Grau (jurisprudência, acórdãos)

## 📐 Melhores Práticas

Consulte o `README_GHERKIN.md` no diretório raiz para boas práticas gerais de Gherkin.

### Específico para 2º Grau
1. **Sempre use a senha "123"** para o 2º Grau
2. **Use URL com "2g"** para cenários do 2º Grau
3. **Referencie "apelação" e "recurso"** ao invés de "processo" quando aplicável
4. **Mencione "acórdão"** para documentos do 2º Grau

## 🐛 Troubleshooting

Para problemas gerais, consulte `README_GHERKIN.md`.

### Erro de autenticação
- Verifique se está usando a senha **123** (não `tjpe1977`)
- Confirme a URL começa com **h06-2g**

### Elemento não encontrado
- Pode ser diferença na estrutura entre 1º e 2º Grau
- Consulte os scripts Python originais em `Selenium_pje_administrador/`

## 📚 Recursos Adicionais

- [Documentação Behave](https://behave.readthedocs.io/)
- [README Principal - Gherkin](../README_GHERKIN.md)
- Scripts de teste originais em `Selenium_pje_administrador/`

## 👥 Contribuição

Ao adicionar novos cenários para 2º Grau:

1. Criar branches descritivos
2. Manter consistência com padrão do 1º Grau
3. Destacar diferenças específicas do 2º Grau
4. Documentar novas funcionalidades

## 📝 Diferenças Implementadas

Este conjunto de features foi adaptado do 1º Grau com as seguintes diferenças:

| Aspecto | 1º Grau | 2º Grau |
|---------|---------|---------|
| URL | h06-1g | h06-2g |
| Senha | tjpe1977 | 123 |
| Processos | Primeiro grau | Apelações/Recursos |
| Sessões | Audiências | Julgamentos |
| Documentos | Sentenças | Acórdãos |
| Jurisprudência | - | ✓ (específico) |
| Certificado Digital | - | ✓ (link extra) |

---

**Última atualização**: 15/07/2026
**Status**: ✅ Pronto para uso
