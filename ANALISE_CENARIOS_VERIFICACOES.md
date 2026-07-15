# 📊 ANÁLISE DETALHADA DE CENÁRIOS E VERIFICAÇÕES POR PAPEL
## Desconsiderando pasta "contador"

Data: 15/07/2026

---

## 1º GRAU - ANÁLISE COMPLETA

### 1️⃣ SELENIUM_PJE_ADMINISTRADOR (1º Grau)

#### Scripts Base (nível raiz)
1. **1_pge_telaPrincipal_label.py** → 11 driver operations
2. **2_pje_login.py** → 4 driver operations  
3. **3_pje_abrir_menu.py** → 11 driver operations

**Subtotal Scripts Base: 3 cenários | 26 verificações**

#### Menu_1_Painel
- 1_pje_painel_menu.py (não listado nos arquivos analisados)

#### Menu_2_Processos (Dentro de Processo_Judicial_Eletronico_1º_Grau)
1. 9_pje_processo_menu.py → 14 driver ops
2. 28_pje_processo_novo_processo.py → 15 driver ops
3. 29_pje_processo_novo_processo_incidental.py → 14 driver ops
4. 30_pje_processo_novo_processo_com_jus_postulandi.py → 13 driver ops
5. 31_pje_processo_nova_liquidacao_e_execucao_trabalhista.py → 12 driver ops
6. 32_pje_processo_nao_protocolado.py → 12 driver ops
7. 33_pje_processo_importar_processo_do_judwin_1º_grau.py → 14 driver ops
8. 34_pje_processo_pesquisar.py → 13 driver ops
9. 35_pje_processo_outras_acoes.py → 15 driver ops
10. 89_pje_processo_outras_acoes_raca.py → 12 driver ops

**Subtotal Menu_2_Processos: 10 cenários | 134 verificações**

#### Menu_3_Atividades
1. 5_pje_atividades_menus.py → 13 driver ops
2. 36_pje_atividades_assinar_documentos_pendentes.py → 12 driver ops
3. 37_pje_atividades_aviso.py → 13 driver ops
4. 38_pje_atividades_consulta_pessoa.py → 14 driver ops
5. 39_pje_atividades_criar_relacao_pessoal.py → 12 driver ops
6. 40_pje_atividades_desunificar_pessoas.py → 12 driver ops
7. 41_pje_atividades_distribuicao_de_expediente.py → 13 driver ops
8. 42_pje_atividades_emitir_certidao.py → 12 driver ops
9. 43_pje_atividades_impressao_de_documento_em_lote.py → 13 driver ops
10. 44_pje_atividades_pauta_de_pericia.py → 12 driver ops
11. 45_pje_atividades_redistribuicao_de_expediente.py → 13 driver ops
12. 46_pje_atividades_registrar_disponibilidade_de_perito.py → 12 driver ops
13. 47_pje_atividades_registrar_indisponibilidade_de_perito.py → 12 driver ops
14. 48_pje_atividades_requisicao_de_antecipacao_de_pagamento_do_perito.py → 13 driver ops
15. 49_pje_atividades_elaborar_RPV_ou_precatorio.py → 12 driver ops
16. 50_pje_atividades_imprimir_RPV_e_precatorio.py → 12 driver ops
17. 51_pje_atividades_simular_valor_a_compensar.py → 12 driver ops
18. 52_pje_atividades_solicitacao_de_antecipacao_de_pagamento_de_pericia.py → 12 driver ops

**Subtotal Menu_3_Atividades: 18 cenários | 225 verificações**

#### Menu_4_Audiências e Sessões
1. 6_pje_audiencias_e_sessoes_menu.py → 13 driver ops
2. 53_pje_audiencias_e_sessoes_acordao.py → 13 driver ops
3. 54_pje_audiencias_e_sessoes_cadastro_de_sessao_de_julgamento.py → 14 driver ops
4. 55_pje_audiencias_e_sessoes_decisao_de_julgamento.py → 12 driver ops
5. 56_pje_audiencias_e_sessoes_tipo_de_julgamento.py → 12 driver ops
6. 57_pje_audiencias_e_sessoes_parametro.py → 12 driver ops
7. 58_pje_audiencias_e_sessoes_publicacao_de_decisoes_em_sessao_em_mural.py → 13 driver ops
8. 59_pje_audiencias_e_sessoes_pendencias_da_sessao_de_julgamento.py → 12 driver ops
9. 60_pje_audiencias_e_sessoes_processos_pautados_em_sessao.py → 13 driver ops
10. 61_pje_audiencias_e_sessoes_relacao_de_julgamento.py → 12 driver ops
11. 62_pje_audiencias_e_sessoes_pauta_de_julgamento.py → 13 driver ops
12. 63_pje_audiencias_e_sessoes_pauta_de_audiencia.py → 12 driver ops

**Subtotal Menu_4_Audiências: 12 cenários | 153 verificações**

#### Menu_5_Configurações
1. 7_pje_configuracao_menu.py → 13 driver ops
2. 64_pje_configuracao_ambiente.py → 12 driver ops
3. 65_pje_configuracao_audiencias_e_sessoes.py → 13 driver ops
4. 66_pje_configuracao_central_de_mandados.py → 12 driver ops
5. 67_pje_configuracao_competencia.py → 12 driver ops
6. 68_pje_configuracao_controle_de_acesso.py → 13 driver ops
7. 69_pje_configuracao_criminal.py → 12 driver ops
8. 70_pje_configuracao_distribuicao.py → 12 driver ops
9. 71_pje_configuracao_documento.py → 12 driver ops
10. 72_pje_configuracao_mobile.py → 12 driver ops
11. 73_pje_configuracao_jurisdicao.py → 13 driver ops
12. 74_pje_configuracao_orgao_julgador.py → 12 driver ops
13. 75_pje_configuracao_orgao_julgador_colegiado.py → 12 driver ops
14. 76_pje_configuracao_orgao_de_representacao.py → 12 driver ops
15. 77_pje_configuracao_motivos_de_isencao.py → 13 driver ops
16. 78_pje_configuracao_pessoa.py → 12 driver ops
17. 79_pje_configuracao_servicos.py → 12 driver ops
18. 80_pje_configuracao_requisitorios.py → 12 driver ops
19. 81_pje_configuracao_procuradoria.py → 13 driver ops
20. 82_pje_configuracao_sistema.py → 12 driver ops
21. 83_pje_configuracao_tabelas_basicas.py → 15 driver ops
22. 84_pje_configuracao_tabelas_judiciais.py → 22 driver ops
23. 85_pje_configuracao_AJG.py → 18 driver ops
24. 86_pje_configuracao_autos_digitais.py → 16 driver ops
25. 88_pje_configuracao_raca.py → 22 driver ops

**Subtotal Menu_5_Configurações: 25 cenários | 342 verificações**

#### Menu_6_Download
1. 8_pje_download_menu.py → 13 driver ops
2. 87_pje_download_area_download.py → 13 driver ops

**Subtotal Menu_6_Download: 2 cenários | 26 verificações**

### **TOTAL ADMINISTRADOR 1º GRAU: 70 cenários | 906 verificações**

---

### 2️⃣ SELENIUM_PJE_ADVOGADO (1º Grau)

#### Scripts Base (nível raiz)
1. **1_pge_telaPrincipal_label.py** → 11 driver ops
2. **2_pje_login.py** → 4 driver ops
3. **3_pje_abrir_menu.py** → 11 driver ops

**Subtotal Scripts Base: 3 cenários | 26 verificações**

#### Menu_1_Painel
1. 4_pje_painel_menus.py → 13 driver ops

**Subtotal: 1 cenário | 13 verificações**

#### Menu_2_Processos
1. 9_pje_processo_menu.py → 14 driver ops
2. 10_pje_processo_pesquisar.py → 13 driver ops

**Subtotal: 2 cenários | 27 verificações**

#### Menu_3_Atividades
1. 5_pje_atividades_menus.py → 15 driver ops
2. 11_pje_atividades_aviso.py → 14 driver ops

**Subtotal: 2 cenários | 29 verificações**

#### Menu_4_Audiências e Sessões
1. 12_pje_audiencias_sessoes_pauta_de_audiencia.py → 13 driver ops
2. 13_pje_audiencias_sessoes_pauta_de_audiencia.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

#### Menu_5_Configurações
1. 6_pje_configuracao_menu.py → 15 driver ops
2. 15_pje_configuracao_pessoa.py → 13 driver ops

**Subtotal: 2 cenários | 28 verificações**

#### Menu_6_Download
1. 7_pje_download_menu.py → 13 driver ops
2. 16_pje_download_area_download.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

### **TOTAL ADVOGADO 1º GRAU: 14 cenários | 175 verificações**

---

### 3️⃣ SELENIUM_PJE_MAGISTRADO (1º Grau)

#### Scripts Base
1. **1_pge_telaPrincipal_label.py** → 11 driver ops

**Subtotal Scripts Base: 1 cenário | 11 verificações**

#### Menu_1_Painel
1. 4_pje_painel_menus.py → 13 driver ops
2. 8_pje_painel_de_expedientes.py → 13 driver ops
3. 9_pje_painel_do_usuario.py → 14 driver ops
4. 10_pje_painel_quadro_de_avisos.py → 13 driver ops

**Subtotal: 4 cenários | 53 verificações**

#### Menu_2_Processos
1. 11_pje_processo_menu.py → 15 driver ops
2. 12_pje_processo_novo_processo.py → 12 driver ops
3. 13_pje_processo_novo_processo_incidental.py → 12 driver ops
4. 14_pje_processo_nao_protocolado.py → 12 driver ops
5. 15_pje_processo_pesquisar.py → 14 driver ops
6. 16_pje_processo_outras_acoes.py → 15 driver ops

**Subtotal: 6 cenários | 80 verificações**

#### Menu_3_Atividades
1. 17_pje_atividades_aviso.py → 12 driver ops
2. 18_pje_atividades_consulta_pessoa.py → 12 driver ops
3. 19_pje_atividades_menus.py → 13 driver ops

**Subtotal: 3 cenários | 37 verificações**

#### Menu_4_Audiências e Sessões
1. 20_pje_audiencias_e_sessoes_pauta_de_audiencia.py → 12 driver ops

**Subtotal: 1 cenário | 12 verificações**

#### Menu_5_Configurações
1. 21_pje_configuracao_menu.py → 12 driver ops
2. 22_pje_configuracao_mobile.py → 13 driver ops

**Subtotal: 2 cenários | 25 verificações**

#### Menu_6_Download
1. 23_pje_download_area_download.py → 13 driver ops
2. 24_pje_download_menu.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

### **TOTAL MAGISTRADO 1º GRAU: 19 cenários | 244 verificações**

---

### 4️⃣ SELENIUM_PJE_PROMOTOR (1º Grau)

#### Scripts Base
1. **1_pge_telaPrincipal_label.py** → 11 driver ops

**Subtotal Scripts Base: 1 cenário | 11 verificações**

#### Menu_2_Processos
1. 9_pje_processo_menu.py → 12 driver ops
2. 17_pje_processo_novo_processo.py → 12 driver ops
3. 18_pje_processo_novo_processo_incidental.py → 12 driver ops
4. 19_pje_processo_nao_protocolado.py → 12 driver ops
5. 20_pje_processo_pesquisar.py → 13 driver ops
6. 21_pje_processo_outras_acoes.py → 15 driver ops

**Subtotal: 6 cenários | 76 verificações**

#### Menu_3_Atividades
1. 5_pje_atividades_menus.py → 12 driver ops
2. 22_pje_atividades_aviso.py → 12 driver ops

**Subtotal: 2 cenários | 24 verificações**

#### Menu_4_Audiências e Sessões
1. 6_pje_audiencias_e_sessoes_menu.py → 12 driver ops
2. 23_pje_audiencias_e_sessoes_pauta_de_audiencia.py → 12 driver ops

**Subtotal: 2 cenários | 24 verificações**

#### Menu_5_Configurações
1. 7_pje_configuracao_menu.py → 12 driver ops
2. 24_pje_configuracao_pessoa.py → 15 driver ops

**Subtotal: 2 cenários | 27 verificações**

#### Menu_6_Download
1. 8_pje_download_menu.py → 13 driver ops
2. 25_pje_download_area_download.py → 12 driver ops

**Subtotal: 2 cenários | 25 verificações**

### **TOTAL PROMOTOR 1º GRAU: 15 cenários | 187 verificações**

---

### 5️⃣ SELENIUM_PJE_OFICIAL_JUSTICA (1º Grau)

#### Scripts Base
1. **1_pge_telaPrincipal_label.py** → 11 driver ops
2. **2_pje_login.py** → 4 driver ops
3. **3_pje_abrir_menu.py** → 11 driver ops

**Subtotal Scripts Base: 3 cenários | 26 verificações**

#### Menu_1_Painel
1. 4_pje_painel_menus.py → 13 driver ops
2. 8_pje_painel_do_oficial_de_justica.py → 14 driver ops

**Subtotal: 2 cenários | 27 verificações**

#### Menu_2_Processos
1. 9_pje_processo_menu.py → 14 driver ops
2. 10_pje_processo_pesquisar.py → 13 driver ops

**Subtotal: 2 cenários | 27 verificações**

#### Menu_3_Atividades
1. 5_pje_atividades_menus.py → 15 driver ops
2. 11_pje_atividades_aviso.py → 14 driver ops
3. 12_pje_atividades_consulta_pessoa.py → 12 driver ops
4. 13_pje_atividades_distribuicao_de_expediente.py → 13 driver ops
5. 14_pje_atividades_redistribuicao_de_expediente.py → 12 driver ops

**Subtotal: 5 cenários | 66 verificações**

#### Menu_4_Configurações (Note: Oficial tem 5 menus sem Audiências)
1. 6_pje_configuracao_menu.py → 15 driver ops
2. 15_pje_configuracao_central_de_mandados.py → 13 driver ops
3. 16_pje_configuracao_mobile.py → 12 driver ops

**Subtotal: 3 cenários | 40 verificações**

#### Menu_5_Download (Note: Oficial tem Download como menu 5)
1. 7_pje_download_menu.py → 13 driver ops
2. 17_pje_download_area_download.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

### **TOTAL OFICIAL DE JUSTIÇA 1º GRAU: 17 cenários | 212 verificações**

---

## 📊 RESUMO 1º GRAU

| Papel | Cenários | Verificações |
|---|---|---|
| **Administrador** | 70 | 906 |
| **Advogado** | 14 | 175 |
| **Magistrado** | 19 | 244 |
| **Promotor** | 15 | 187 |
| **Oficial de Justiça** | 17 | 212 |
| **TOTAL 1º GRAU** | **135** | **1.724** |

---

## 2º GRAU - ANÁLISE COMPLETA

### 1️⃣ SELENIUM_PJE_ADMINISTRADOR (2º Grau)

#### Scripts Base
1. **1_pge_telaPrincipal_label.py** → 10 driver ops (similar ao 1º Grau)
2. **2_pje_login.py** → 4 driver ops
3. **3_pje_abrir_menu.py** → 11 driver ops

**Subtotal Scripts Base: 3 cenários | 25 verificações**

#### Menu_6_Download
1. 8_pje_download_menu.py → 13 driver ops
2. 87_pje_download_area_download.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

### **TOTAL ADMINISTRADOR 2º GRAU: 5 cenários | 51 verificações**

---

### 2️⃣ SELENIUM_PJE_ADVOGADO (2º Grau)

#### Scripts Base (similaridade com 1º Grau)
1. **1_pge_telaPrincipal_label.py** → 10 driver ops
2. **2_pje_login.py** → 4 driver ops
3. **3_pje_abrir_menu.py** → 11 driver ops

**Subtotal Scripts Base: 3 cenários | 25 verificações**

#### Menu_1_Painel
1. 4_pje_painel_menus.py → 13 driver ops

**Subtotal: 1 cenário | 13 verificações**

#### Menu_2_Processos
1. 9_pje_processo_menu.py → 14 driver ops
2. 10_pje_processo_pesquisar.py → 13 driver ops

**Subtotal: 2 cenários | 27 verificações**

#### Menu_3_Atividades
1. 5_pje_atividades_menus.py → 15 driver ops
2. 11_pje_atividades_aviso.py → 14 driver ops

**Subtotal: 2 cenários | 29 verificações**

#### Menu_4_Audiências e Sessões
1. 12_pje_audiencias_sessoes_pauta_de_audiencia.py → 13 driver ops
2. 13_pje_audiencias_sessoes_pauta_de_audiencia.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

#### Menu_5_Configurações
1. 6_pje_configuracao_menu.py → 15 driver ops
2. 15_pje_configuracao_pessoa.py → 13 driver ops

**Subtotal: 2 cenários | 28 verificações**

#### Menu_6_Download
1. 7_pje_download_menu.py → 13 driver ops
2. 16_pje_download_area_download.py → 13 driver ops

**Subtotal: 2 cenários | 26 verificações**

### **TOTAL ADVOGADO 2º GRAU: 14 cenários | 174 verificações**

---

### 3️⃣ SELENIUM_PJE_PROMOTOR (2º Grau)

#### Scripts Base (similar ao 1º Grau)
1. **1_pge_telaPrincipal_label.py** → 10 driver ops

**Subtotal Scripts Base: 1 cenário | 10 verificações**

#### Menu_2_Processos (mesmo que 1º Grau)
1. 9_pje_processo_menu.py → 12 driver ops
2. 17_pje_processo_novo_processo.py → 12 driver ops
3. 18_pje_processo_novo_processo_incidental.py → 12 driver ops
4. 19_pje_processo_nao_protocolado.py → 12 driver ops
5. 20_pje_processo_pesquisar.py → 13 driver ops
6. 21_pje_processo_outras_acoes.py → 15 driver ops

**Subtotal: 6 cenários | 76 verificações**

#### Menu_3_Atividades
1. 5_pje_atividades_menus.py → 12 driver ops
2. 22_pje_atividades_aviso.py → 12 driver ops

**Subtotal: 2 cenários | 24 verificações**

#### Menu_4_Audiências e Sessões
1. 6_pje_audiencias_e_sessoes_menu.py → 12 driver ops
2. 23_pje_audiencias_e_sessoes_pauta_de_audiencia.py → 12 driver ops

**Subtotal: 2 cenários | 24 verificações**

#### Menu_5_Configurações
1. 7_pje_configuracao_menu.py → 12 driver ops
2. 24_pje_configuracao_pessoa.py → 15 driver ops

**Subtotal: 2 cenários | 27 verificações**

#### Menu_6_Download
1. 8_pje_download_menu.py → 13 driver ops
2. 25_pje_download_area_download.py → 12 driver ops

**Subtotal: 2 cenários | 25 verificações**

### **TOTAL PROMOTOR 2º GRAU: 15 cenários | 186 verificações**

---

## 📊 RESUMO 2º GRAU

| Papel | Cenários | Verificações |
|---|---|---|
| **Administrador** | 5 | 51 |
| **Advogado** | 14 | 174 |
| **Promotor** | 15 | 186 |
| **TOTAL 2º GRAU** | **34** | **411** |

---

## 🎯 RESUMO GERAL (Desconsiderando pasta CONTADOR)

### Por Papel

| Papel | 1º Grau Cenários | 1º Grau Verif. | 2º Grau Cenários | 2º Grau Verif. | **TOTAL** |
|---|---|---|---|---|---|
| Administrador | 70 | 906 | 5 | 51 | **75 cenários / 957 verif.** |
| Advogado | 14 | 175 | 14 | 174 | **28 cenários / 349 verif.** |
| Magistrado | 19 | 244 | 0 | 0 | **19 cenários / 244 verif.** |
| Promotor | 15 | 187 | 15 | 186 | **30 cenários / 373 verif.** |
| Oficial de Justiça | 17 | 212 | 0 | 0 | **17 cenários / 212 verif.** |
| **TOTAL GERAL** | **135** | **1.724** | **34** | **411** | **169 cenários / 2.135 verif.** |

---

## 📈 VISUALIZAÇÃO

```
1º GRAU:
├── Administrador: 70 cenários (906 verificações) ⭐ MAIOR
├── Advogado:      14 cenários (175 verificações)
├── Magistrado:    19 cenários (244 verificações)
├── Promotor:      15 cenários (187 verificações)
├── Oficial Just:  17 cenários (212 verificações)
└── TOTAL: 135 cenários | 1.724 verificações

2º GRAU:
├── Administrador: 5 cenários (51 verificações) ⚠️ MENOR
├── Advogado:      14 cenários (174 verificações)
└── Promotor:      15 cenários (186 verificações)
└── TOTAL: 34 cenários | 411 verificações

═════════════════════════════════════════
PROJETO TOTAL: 169 cenários | 2.135 verificações ✅
```

---

## 🔍 ANÁLISE DETALHADA

### Distribuição de Cenários

**1º GRAU (135 cenários)**
- Administrador domina com 52% dos cenários (70/135)
- Magistrado em segundo com 14% (19/135)
- Oficial de Justiça com 13% (17/135)
- Promotor com 11% (15/135)
- Advogado com 10% (14/135)

**2º GRAU (34 cenários)**
- Advogado e Promotor empatados com 41% cada (14 e 15 cenários)
- Administrador com apenas 15% (5 cenários)
- Magistrado e Oficial ausentes (2º Grau não tem essas roles)

### Distribuição de Verificações

**Por Menu (1º Grau Admin - 906 verificações)**
- Menu_5_Configurações: 342 (38%) - MAIOR
- Menu_3_Atividades: 225 (25%)
- Menu_4_Audiências: 153 (17%)
- Menu_2_Processos: 134 (15%)
- Scripts Base + Menu_1 + Menu_6: 52 (6%)

### Verificações Médias

**Por Cenário**
- 1º Grau: 1.724 ÷ 135 = **12,8 verificações/cenário**
- 2º Grau: 411 ÷ 34 = **12,1 verificações/cenário**
- **Média Global: 12,6 verificações/cenário**

---

## 📊 COMPARATIVO COM CENÁRIOS GHERKIN

| Métrica | Scripts Atuais | Gherkin | Total |
|---|---|---|---|
| **Cenários** | 169 | 52 | 221 |
| **Verificações** | 2.135 | 130 | 2.265 |
| **Média/Cenário** | 12,6 | 2,5 | 10,2 |

**Nota**: Gherkin tem verificações lógicas de alto nível, enquanto scripts têm operações granulares.

---

## ✅ CONCLUSÃO

### Status Atual do Projeto

- **Total de Cenários (Scripts)**: 169
- **Total de Verificações (Driver ops)**: 2.135
- **Cenários Gherkin Criados**: 52
- **Verificações Gherkin**: 130

### Distribuição Equilibrada?

✅ **1º Grau**: Muito bem coberto (135 cenários)
⚠️ **2º Grau**: Menos cenários (34), principalmente admin

✅ **Administrador**: Extremamente completo (75 cenários)
⚠️ **Oficial de Justiça**: Apenas 1º Grau (17 cenários)

---

**Gerado em**: 15/07/2026
**Análise**: Desconsiderando pasta "contador"
**Status**: ✅ ANÁLISE CONCLUÍDA
