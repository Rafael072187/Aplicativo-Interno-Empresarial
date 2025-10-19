import streamlit as st

nome_usuario = st.session_state.get("usuario_logado", None)

coluna_esquerda, coluna_direta = st.columns([1, 1.6])

coluna_esquerda.title("Aplicativo Interno Empresarial")
if nome_usuario:
    coluna_esquerda.write(f"### Bem Vindo, {nome_usuario}")

botao_dashboards = coluna_esquerda.button("Dashboards Projetos")
botao_indicadores = coluna_esquerda.button("Principais Indicadores")

if botao_dashboards:
    st.switch_page("dashboard.py")
if botao_indicadores:
    st.switch_page("indicadores.py")

container = coluna_direta.container(border=True)
container.image(r"imagens\interno-na-sua-empresa.png")