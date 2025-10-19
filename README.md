<center>
  <h1 style="font-size:2.4em; margin-bottom:0.1em;">🏢 Aplicativo Interno Empresarial</h1>
  <p style="margin-top:0.2em; font-size:1.05em; color:#555;">
    Plataforma corporativa em <b>Streamlit</b> com autenticação de usuários, dashboards financeiros e monitoramento de indicadores operacionais.
  </p>
  <p>
    <a href="https://github.com/Rafael072187/Aplicativo-Interno-Empresarial" style="background:#24292F;color:#fff;padding:8px 14px;border-radius:8px;text-decoration:none;font-weight:600;">
      🔗 Repositório no GitHub
    </a>
  </p>
</center>

<hr>

## 🧭 Tabela de Conteúdos

- [Descrição](#-descrição)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Tecnologias](#-tecnologias)
- [Como contribuir](#-como-contribuir)
- [Autor](#-autor)
- [Observações](#-observações)

---

## 📘 Descrição

<details>
<summary><b>Resumo</b></summary>

O **Aplicativo Interno Empresarial** é uma solução corporativa desenvolvida com **Streamlit**, projetada para **monitorar projetos, analisar indicadores financeiros e centralizar informações empresariais** em um ambiente seguro e intuitivo.

O sistema possui:

- **Autenticação de usuários** com permissões administrativas (via *streamlit-authenticator*);
- **Dashboards interativos** com filtros por setor, status e período;
- **Gestão de contas internas** e controle de acesso;
- **Gráficos dinâmicos** gerados com *Plotly*;
- **Banco de dados relacional (SQLite + SQLAlchemy)** para persistência de informações;
- **Integração com planilhas Excel (Base.xlsx)** para ingestão e atualização de dados.

Ideal para empresas que buscam **transformar planilhas em relatórios visuais interativos**, otimizando o acompanhamento de resultados e decisões estratégicas.

</details>

---

## ⚙️ Instalação

<details>
<summary><b>Passo a passo (Linux / macOS / Windows)</b></summary>

1. Clone o repositório:
   ```bash
   git clone https://github.com/Rafael072187/Aplicativo-Interno-Empresarial.git
   cd Aplicativo-Interno-Empresarial
Crie e ative um ambiente virtual (recomendado):

Windows (PowerShell):

bash
Copiar código
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux:

bash
Copiar código
python3 -m venv .venv
source .venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Certifique-se de que o arquivo Base.xlsx esteja presente na raiz do projeto.
Ele contém os dados base utilizados pelos dashboards.

Execute o aplicativo:

bash
Copiar código
streamlit run main.py
</details>
🖥️ Uso
<details> <summary><b>Como usar o projeto</b></summary>
Após iniciar a aplicação, acesse o endereço exibido no terminal (geralmente http://localhost:8501).

Funcionalidades principais:

Login e autenticação de usuários;

Visualização de dashboards financeiros e operacionais;

Indicadores de desempenho e status de projetos;

Filtros dinâmicos por período, setor e status;

Controle de acesso por tipo de usuário.

</details> <p align="center" style="margin-top:14px;"> <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="90" alt="ícone ilustrativo"> <br> <i>Exemplo de interface de dashboard (baseada em Streamlit e Plotly).</i> </p>
🛠️ Tecnologias
<details> <summary><b>Stack principal</b></summary>
Linguagem: Python 3.8+

Framework: Streamlit

Visualização: Plotly

Banco de Dados: SQLite + SQLAlchemy

Autenticação: Streamlit-Authenticator

Manipulação de Dados: Pandas

Fonte de Dados: Excel (Base.xlsx)

Arquivos principais:

main.py — ponto de entrada da aplicação

dashboard.py — painéis e visualizações financeiras

indicadores.py — lógica dos KPIs e indicadores

models.py — estrutura ORM com SQLAlchemy

data_loader.py — leitura e atualização de dados Excel

config.toml — tema e configurações visuais

</details>
🤝 Como contribuir
<details> <summary><b>Guia rápido</b></summary>
Faça um fork do repositório

Crie uma nova branch:

bash
Copiar código
git checkout -b feature/nova-funcionalidade
Faça as alterações e commit:

bash
Copiar código
git commit -m "feat: adiciona nova funcionalidade"
Envie a branch:

bash
Copiar código
git push origin feature/nova-funcionalidade
Abra um Pull Request 🚀

</details>
👤 Autor
<details> <summary><b>Contatos</b></summary> <p> <b>Rafael Bittencourt de Araújo</b> — desenvolvedor do projeto.<br> GitHub: <a href="https://github.com/Rafael072187" target="_blank">github.com/Rafael072187</a><br> </p> </details>
📝 Observações
✅ Projeto ideal para uso corporativo interno e análise de indicadores empresariais.
🔧 Facilmente adaptável para outras áreas (RH, Vendas, Produção, etc.).
⚠️ Para ambientes de produção, configure variáveis de ambiente e use banco de dados seguro (PostgreSQL ou MySQL).

<p align="center" style="margin-top:18px;"> <a href="https://github.com/Rafael072187/Aplicativo-Interno-Empresarial" style="background:#0b5fff;color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none;font-weight:600;"> Ver repositório </a> </p> <p align="center" style="margin-top:14px;color:#666;"> Estrutura gerada automaticamente com base no repositório analisado. </p> ```
