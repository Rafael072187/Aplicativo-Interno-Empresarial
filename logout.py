import streamlit as st

st.title("🚪 Logout")

if "logado" in st.session_state:
    st.session_state.clear()
    st.success("Você saiu com sucesso!")
    st.markdown("[Voltar ao login](main.py)")
else:
    st.warning("Você não está logado.")
