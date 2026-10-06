<p align="center">
  <img src="assets/logo_mesafartai.png" alt="Logo MESAFARTAI" width="220">
</p>

# MESAFARTAI - Logística e Inteligência Assistiva no Combate à Fome

> *"A tecnologia só alcança seu propósito mais elevado quando é utilizada para resolver dores humanas reais e salvar vidas."*

**Disciplina:** Machine Learning & Chatbots
**Turma:** Terça-feira

---

## 📌 Sobre o Projeto

Todos os dias, toneladas de alimentos próprios para consumo são descartadas por supermercados, restaurantes, feirantes e produtores por estarem próximos da validade, terem pequenos defeitos estéticos ou por excesso de estoque. Ao mesmo tempo, ONGs, abrigos e cozinhas comunitárias enfrentam escassez de suprimentos.

O gargalo não é a falta de comida, e sim a **falta de logística ágil e comunicação eficiente**.

O **MESAFARTAI** é uma aplicação conversacional em Python que:

1. **Entende mensagens informais** de doadores e ONGs via chat (NLU com TF-IDF + classificador Scikit-Learn);
2. **Protege a conversa** com uma trava de confiança (*threshold* < 0.60 → resposta de *fallback*);
3. **Extrai automaticamente** alimentos, quantidades (kg, caixas, unidades) e validades (hoje, amanhã, 18h) via **Regex**;
4. **Realiza o matchmaking logístico** com **KNN**, direcionando a doação para a ONG mais próxima;
5. **Persiste tudo em SQLite3** (usuários, doações e matches) e exibe uma interface/dashboard em **Streamlit**.

## 🌍 Alinhamento com a ODS 2 da ONU

Este projeto está diretamente alinhado à **ODS 2 – Fome Zero e Agricultura Sustentável**, da Agenda 2030 da ONU, em especial:

- **Meta 2.1:** acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis, a alimentos seguros, nutritivos e suficientes durante todo o ano;
- **Contribuição indireta à Meta 12.3 (ODS 12):** reduzir pela metade o desperdício de alimentos no varejo e no consumidor.

Ao reduzir o atrito para doar (basta mandar uma mensagem no chat) e ao encontrar automaticamente a ONG mais próxima, o MESAFARTAI transforma desperdício em refeição.

## 👥 Integrantes do Grupo – NPC

| Nome Completo | RA | Curso |
|---|---|---|
| Pedro Vitor da Silva Oliveira | 130785 | Ciência da Computação |
| Nicollas Hardt Urnau | 117763 | Ciência da Computação |
| Caio Gabriel Souza dos Santos | 118316 | Ciência da Computação |

## 🗂️ Estrutura do Repositório

```
PROJETO-MESAFARTAI/
├── docs/                         # Documentação do projeto
│   ├── regras.txt                # Requisitos da etapa 1, regras internas e papéis do grupo
│   ├── escopo_projeto.md         # Problema, público-alvo, intenções e prompt do logo
│   ├── arquitetura_mesafartai.png
│   └── diag_fluxo_mesafartai.png
├── assets/
│   └── logo_mesafartai.png       # Logotipo gerado via IA
├── src/
│   ├── database.py               # Criação das tabelas e seeds do SQLite  (06/10 ✅)
│   ├── nlu.py                    # Pipeline TF-IDF + Classificador + Threshold (13/10)
│   ├── regex_entities.py         # Extração de entidades via Regex (27/10)
│   ├── matchmaking.py            # Algoritmo KNN de proximidade (27/10)
│   └── app.py                    # Interface Streamlit e Dashboard (03/11)
├── data/
│   └── dataset_intencoes.csv     # Dataset de treino do classificador (13/10)
├── .gitignore
├── README.md
└── requirements.txt
```

## 🏗️ Arquitetura e Fluxo de Dados

| Arquitetura em camadas | Fluxo de dados simplificado |
|---|---|
| ![Arquitetura](docs/arquitetura_mesafartai.png) | ![Fluxo](docs/diag_fluxo_mesafartai.png) |

## ▶️ Como Executar

```bash
# 1. Clonar o repositório
git clone https://github.com/Th3L0ck1/PROJETO-MESAFARTAI.git
cd PROJETO-MESAFARTAI

# 2. (Opcional) Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Inicializar o banco de dados com a carga de teste
python src/database.py
```

Saída esperada:

```
✅ Dados iniciais de teste inseridos com sucesso!
✅ Banco de dados 'mesafartai.db' inicializado com sucesso!
   - usuarios: 4 registro(s)
   - doacoes: 2 registro(s)
   - matches: 0 registro(s)
```

## 📅 Cronograma

| Data | Entrega | Status |
|---|---|---|
| 06/10 | Kickoff, documentação, arquitetura, BD SQLite e carga inicial | ✅ |
| 13/10 | Pipeline NLU (Classificação de Intenções + Threshold/Fallback) | ⏳ |
| 27/10 | Extração Regex + KNN de Matchmaking + Entrega final AC-3 | ⏳ |
| 03/11 | Interface Web Conversacional no Streamlit | ⏳ |
| 10/11 | Dashboard Logístico de Impacto Social + Testes de Estresse | ⏳ |
| 17/11 | Demo Day (Pitching) + Entrega final AC-4 | ⏳ |
