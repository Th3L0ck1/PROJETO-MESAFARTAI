# =============================================================================
# PAINEL DE DOAÇÕES - Aula de Streamlit
# Rodar com:  streamlit run app_streamlit.py
# =============================================================================
import streamlit as st
import pandas as pd
from datetime import datetime

# 0. CONFIGURAÇÃO DA PÁGINA (deve ser o primeiro comando do Streamlit)
st.set_page_config(page_title="Painel de Doações", page_icon="🥫")

st.title("Painel de Doações de Alimentos")
st.caption("Exemplo de: session_state, colunas, sidebar, formulário, métricas e gráfico")

# 1. MEMÓRIA DA SESSÃO
# O Streamlit executa o script do zero a cada clique. Variáveis comuns são
# recriadas; o st.session_state guarda os dados entre as execuções.
if "doacoes" not in st.session_state:
    st.session_state.doacoes = []  # lista de dicionários (uma doação por item)

# 2. BARRA LATERAL (sidebar): configurações e botão de reset
st.sidebar.header("Configurações")
meta = st.sidebar.slider("Meta de arrecadação (kg)", min_value=50, max_value=500, value=200, step=10)

if st.sidebar.button("Zerar painel"):
    st.session_state.doacoes = []  # esvazia a memória

# 3. FORMULÁRIO DE ENTRADA, organizado em 2 colunas
st.subheader("Registrar nova doação")
col1, col2 = st.columns(2)

with col1:
    doador = st.text_input("Nome do doador")
    categoria = st.selectbox("Categoria", ["Arroz", "Feijão", "Macarrão", "Óleo", "Enlatados", "Outros"])

with col2:
    # Limite máximo de cada doação ajustado para 25 kg conforme Tarefa 1
    quantidade = st.number_input("Quantidade (kg)", min_value=1, max_value=25, value=5)

# 4. AÇÃO DO BOTÃO: st.button devolve True apenas no momento do clique
if st.button("Registrar doação", type="primary"):
    if doador.strip() == "":
        st.warning("Informe o nome do doador.")
    else:
        total_antes = sum(d["Kg"] for d in st.session_state.doacoes)

        st.session_state.doacoes.append({
            "Hora": datetime.now().strftime("%H:%M:%S"),
            "Doador": doador.strip(),
            "Categoria": categoria,
            "Kg": quantidade,
        })
        st.success(f"Obrigado, {doador.strip()}! Doação de {quantidade} kg registrada.")

        # Comemora só no momento em que a meta é atingida
        if total_antes < meta <= total_antes + quantidade:
            st.balloons()

# 5. INDICADORES (métricas) calculados a partir da memória
total = sum(d["Kg"] for d in st.session_state.doacoes)
qtd_doacoes = len(st.session_state.doacoes)
faltam = max(meta - total, 0)

st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Total arrecadado", f"{total} kg")
m2.metric("Nº de doações", qtd_doacoes)
m3.metric("Faltam para a meta", f"{faltam} kg")

# Barra de progresso: o valor precisa estar entre 0.0 e 1.0
st.progress(min(total / meta, 1.0), text=f"{min(total / meta, 1.0):.0%} da meta de {meta} kg")

# 6. TABELA E GRÁFICO (só aparecem se houver dados)
if st.session_state.doacoes:
    df = pd.DataFrame(st.session_state.doacoes)

    st.subheader("Doações por categoria")
    st.bar_chart(df.groupby("Categoria")["Kg"].sum())

    st.subheader("Histórico")
    st.dataframe(df, width="stretch", hide_index=True)
else:
    st.info("Nenhuma doação registrada ainda. Use o formulário acima!")
