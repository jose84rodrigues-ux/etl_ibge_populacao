# ETL - População IBGE

Projeto de Engenharia de Dados utilizando Python, Pandas e SQLite.

## 🎯 Objetivo

Construir um pipeline ETL para tratar dados públicos do IBGE,
eliminando registros inválidos e disponibilizando os dados
para análise SQL.

---

## 🏗 Arquitetura do Projeto

Raw → Transform → Processed → SQLite → SQL



```  
etl_ibge_populacao/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── transform_populacao.py
│   ├── load_sqlite.py
│   └── view_sqlite.py
│
├── requirements.txt
└── README.md
```









## ⚙️ Tecnologias Utilizadas

- Python
- Pandas
- SQLite
- Git

---

## 🔄 Pipeline

### 1️⃣ Transformação
- Leitura da camada raw
- Tratamento de encoding
- Remoção de linhas inválidas
- Conversão de tipos
- Salvamento na camada processed

### 2️⃣ Load
- Inserção dos dados tratados no SQLite

### 3️⃣ Análise
- Consultas SQL para ranking e crescimento populacional

---

## 🚀 Como Executar

```bash
python scripts/transform_populacao.py
python scripts/load_sqlite.py
python scripts/view_sqlite.py
