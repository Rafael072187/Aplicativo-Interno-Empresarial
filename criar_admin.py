from models import session, Usuario
from passlib.hash import bcrypt_sha256

try:
    senha_criptografada = bcrypt_sha256.hash("123456")

    usuario = Usuario(
        nome="Admin",
        senha=senha_criptografada,
        email="admin@empresa.com",
        admin=True
    )

    session.add(usuario)
    session.commit()
    print("✅ Admin criado com sucesso!")
except Exception as e:
    print("❌ Erro ao criar admin:", e)
