from models import session, Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["123456"]).generate()[0]
usuario = Usuario(nome="Rafa2", senha=senha_criptografada, email="teste3@gmail.com", admin=False)
session.add(usuario)
session.commit()