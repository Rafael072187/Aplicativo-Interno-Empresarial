import streamlit as st
from passlib.hash import bcrypt_sha256
from models import session, Usuario
from data_loader import carregar_dados

st.set_page_config(page_title="Aplicativo Interno Empresarial", layout="wide")

# === Inicializa estado da sessão ===
if "logado" not in st.session_state:
    st.session_state["logado"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "nome" not in st.session_state:
    st.session_state["nome"] = None
if "admin" not in st.session_state:
    st.session_state["admin"] = False
if "bemvindo_exibido" not in st.session_state:
    st.session_state["bemvindo_exibido"] = False  # <-- controle de exibição única

# === Tela de login (só aparece se não estiver logado) ===
if not st.session_state["logado"]:
    st.title("🔐 Login no Aplicativo Interno Empresarial")
    st.markdown("---")

    with st.form("login_form"):
        email_input = st.text_input("Email")
        senha_input = st.text_input("Senha", type="password")
        submit = st.form_submit_button("Entrar")

    if submit:
        if not email_input or not senha_input:
            st.error("Preencha email e senha.")
        else:
            usuario = session.query(Usuario).filter_by(email=email_input).first()
            if usuario is None:
                st.error("Usuário não encontrado.")
            else:
                try:
                    if bcrypt_sha256.verify(senha_input, usuario.senha):
                        st.session_state["logado"] = True
                        st.session_state["username"] = usuario.email
                        st.session_state["nome"] = usuario.nome
                        st.session_state["admin"] = usuario.admin
                        st.session_state["bemvindo_exibido"] = False  # reset ao logar
                        st.success("✅ Login realizado com sucesso!")
                        st.rerun()
                    else:
                        st.error("Senha incorreta.")
                except Exception as e:
                    st.error(f"Erro ao verificar senha: {e}")

# === Após login ===
if st.session_state["logado"]:
    base = carregar_dados()
    nome = st.session_state["nome"]
    admin = st.session_state["admin"]

    # Exibe “Bem-vindo” só uma vez após login
    if not st.session_state["bemvindo_exibido"]:
        if admin:
            st.success(f"Bem-vindo novamente, {nome}! (Admin)")
        else:
            st.success(f"Bem-vindo novamente, {nome}!")
        st.session_state["bemvindo_exibido"] = True  # <-- garante que só aparece uma vez

    # === Definição de páginas ===
    if admin:
        pg = st.navigation(
            {
                "Home": [st.Page("homepage.py", title="Aplicativo Interno Empresarial")],
                "Dashboards": [
                    st.Page("dashboard.py", title="Dashboard"),
                    st.Page("indicadores.py", title="Indicadores"),
                ],
                "Conta": [
                    st.Page("criar_conta.py", title="Criar Conta"),  # só admin
                    st.Page("logout.py", title="Sair"),
                ],
            }
        )
    else:
        pg = st.navigation(
            {
                "Home": [st.Page("homepage.py", title="Aplicativo Interno Empresarial")],
                "Dashboards": [
                    st.Page("dashboard.py", title="Dashboard"),
                    st.Page("indicadores.py", title="Indicadores"),
                ],
                "Conta": [st.Page("logout.py", title="Sair")],  # usuário comum sem criar conta
            }
        )

    pg.run()
