from sqlalchemy import create_engine, Integer, String, Boolean, Column
from sqlalchemy.orm import sessionmaker, declarative_base

# Caminho absoluto para o banco de dados SQLite
db = create_engine("sqlite:///C:/Users/Rafael/Desktop/PYTHONARQUIVOS/Projetos/Aplicativo Interno Empresarial/database/meubanco.db")

# Cria sessão de conexão
Session = sessionmaker(bind=db)
session = Session()

# Base ORM
Base = declarative_base()

# Modelo da tabela de usuários
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, senha, email, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin

# Cria as tabelas no banco
Base.metadata.create_all(bind=db)

print("✅ Banco de dados e tabela 'usuarios' criados com sucesso.")
