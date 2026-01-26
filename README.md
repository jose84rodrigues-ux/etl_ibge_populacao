# 📊 ETL – População IBGE (Projeto de Engenharia de Dados)

## 📌 Visão Geral

Este projeto tem como objetivo demonstrar um **pipeline ETL (Extract, Transform, Load)** aplicado a dados populacionais do IBGE, utilizando uma base de dados **fictícia**, com foco em boas práticas de **Engenharia de Dados** para portfólio profissional.

O pipeline realiza:

* Extração de dados brutos (CSV)
* Tratamento e padronização dos dados
* Carga em um banco de dados SQLite

---

## 🧱 Arquitetura do Projeto

```
etl_ibge_populacao/
│
├── data/
│   ├── raw/            # Dados brutos (não versionados)
│   └── processed/      # Dados tratados
│
├── scripts/
│   ├── extract_populacao.py   # Extração dos dados
│   ├── transform_populacao.py # Transformação dos dados
│   └── load_sqlite.py          # Carga no banco SQLite
│
├── database/           # Banco de dados SQLite gerado
├── venv/               # Ambiente virtual (ignorado no Git)
├── requirements.txt    # Dependências do projeto
├── .gitignore
└── README.md
```

---

## 🔄 Pipeline ETL

### 1️⃣ Extract

* Leitura de arquivo CSV da camada `data/raw`
* Validação básica de estrutura

### 2️⃣ Transform

* Padronização de nomes de colunas
* Conversão de tipos de dados
* Limpeza e organização dos registros
* Geração do arquivo tratado em `data/processed`

### 3️⃣ Load

* Leitura do CSV tratado
* Criação de tabela no SQLite
* Inserção dos dados no banco

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* **Pandas**
* **SQLite**
* **Git & GitHub**
* **VS Code**

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/etl_ibge_populacao.git
cd etl_ibge_populacao
```

### 2️⃣ Criar e ativar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o pipeline ETL

```bash
python scripts/extract_populacao.py
python scripts/transform_populacao.py
python scripts/load_sqlite.py
```

---

## 📂 Dados

* Os dados utilizados são **fictícios**, inspirados em dados públicos do IBGE
* Arquivos brutos não são versionados por boas práticas

---

## 📈 Possíveis Evoluções

* Automação com Airflow
* Testes de qualidade de dados
* Integração com Power BI
* Deploy em cloud (AWS / GCP)

---

## 👨‍💻 Autor

**José Rodrigues**
Projeto desenvolvido para fins de estudo e portfólio em Engenharia de Dados.

---

## 📝 Licença

Este projeto é de uso educacional e demonstrativo.
