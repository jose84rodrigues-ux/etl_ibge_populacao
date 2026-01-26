# 📊 ETL – População IBGE (Projeto de Engenharia de Dados)

Este projeto implementa uma **pipeline ETL completa** utilizando dados de população inspirados no IBGE, com foco em boas práticas de **engenharia de dados**, versionamento e organização em camadas.

---

## 🎯 Objetivo do Projeto

Construir um pipeline de dados capaz de:

- Extrair dados populacionais (camada RAW)
- Transformar e padronizar os dados (camada PROCESSED)
- Carregar os dados em um banco relacional (SQLite)
- Garantir organização, reprodutibilidade e versionamento no GitHub

Projeto desenvolvido com foco em **portfólio profissional**.

---

## 🏗 Arquitetura do Projeto

etl_ibge_populacao/
├── data/
│ ├── raw/ # Dados brutos
│ └── processed/ # Dados tratados
├── database/
│ └── populacao.db # Banco SQLite
├── scripts/
│ ├── extract_populacao.py
│ ├── transform_populacao.py
│ └── load_sqlite.py
├── README.md
├── requirements.txt
---

## 🔄 Pipeline ETL

### 1️⃣ Extract
- Leitura de dados CSV brutos
- Validação de estrutura
- Salvamento na camada `raw`

### 2️⃣ Transform
- Padronização de colunas
- Limpeza de dados
- Tratamento de tipos
- Geração da camada `processed`

### 3️⃣ Load
- Leitura do CSV tratado
- Criação de banco SQLite
- Carga dos dados em tabela relacional
- Validação de registros carregados

---

## 🛠 Tecnologias Utilizadas

- **Python 3.11**
- **Pandas**
- **SQLite**
- **Git & GitHub**
- **VS Code**

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/etl_ibge_populacao.git
cd etl_ibge_populacao
