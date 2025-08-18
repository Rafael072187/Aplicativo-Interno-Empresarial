📊 Aplicativo Interno Empresarial — Plataforma de Indicadores Gerenciais

Este projeto consiste em uma plataforma corporativa desenvolvida em Streamlit, com suporte a autenticação de usuários e dashboards interativos voltados ao monitoramento de projetos e análise de indicadores financeiros.

A aplicação oferece controle de acesso por tipo de usuário, múltiplas páginas integradas e visualizações gráficas avançadas com suporte a filtros dinâmicos e métricas estratégicas.

🧩 Principais Funcionalidades

🔐 Autenticação segura de usuários via streamlit-authenticator e banco de dados SQLite

👤 Gestão de contas: criação de usuários com ou sem permissão de administrador

📈 Dashboards interativos com filtros por setor, status e ano de execução

📊 Indicadores financeiros e operacionais com gráficos dinâmicos

📁 Persistência de dados em banco relacional com SQLAlchemy (ORM)

🎨 Interface adaptada ao tema escuro, com layout moderno e responsivo

🧮 Integração com planilhas (Base.xlsx) para ingestão de dados

📁 Estrutura de Diretórios
📦 aplicativo-empresarial/
├── 📜 main.py                # Ponto de entrada da aplicação
├── 📜 homepage.py           # Tela inicial de boas-vindas e navegação
├── 📜 dashboard.py          # Dashboard financeiro e de projetos
├── 📜 indicadores.py        # Indicadores de desempenho e funil de status
├── 📜 criar_conta.py        # Página de criação de novas contas (admin)
├── 📜 criar_admin.py        # Script auxiliar para criar administradores
├── 📜 models.py             # Definição do modelo de dados (ORM)
├── 📜 data_loader.py        # Carregamento de dados a partir de planilhas
├── 📜 requirements.txt      # Dependências da aplicação
├── 📜 config.toml           # Configuração de tema e aparência
├── 📁 imagens/              # Imagens utilizadas nos cards e interface
└── 📄 Base.xlsx             # Base de dados principal (entrada)

🧪 Tecnologias Utilizadas
Tecnologia	Finalidade
Streamlit	Construção da interface web interativa
Plotly	Geração de gráficos dinâmicos e responsivos
SQLAlchemy	ORM para persistência em banco de dados
SQLite	Armazenamento local de usuários
Pandas	Manipulação de dados tabulares
streamlit-authenticator	Autenticação e controle de acesso

💻 Instruções de Execução

1. Instale as dependências
pip install -r requirements.txt

2. Prepare a base de dados

Certifique-se de que o arquivo Base.xlsx está na raiz do projeto.

A planilha deve conter, no mínimo, as seguintes colunas:

Setor | Status | Data Chegada | Valor Orçado | Valor Negociado | Desconto Concedido | Código Projeto

3. Execute o sistema

streamlit run main.py

📊 Dashboards Disponíveis

Dashboard de Projetos (dashboard.py)

Filtros: Setor, Status e Ano

Gráficos:

Área acumulada de Valor Negociado

Barras comparativas: Valor Orçado vs Valor Pago

Indicadores:

Total pago e total em descontos no ano selecionado

Indicadores Gerais (indicadores.py)

Cards com KPIs:

Total de oportunidades

Projetos em andamento

Projetos finalizados

Valores orçados, pagos e descontos

Gráfico funil por status do projeto

🧠 Controle de Navegação

A navegação entre páginas é controlada via permissões:

Administradores têm acesso completo:

Home, Dashboards, Indicadores, Criar Conta, Logout

Usuários comuns:

Home, Dashboards, Indicadores, Logout

Controle realizado no main.py com base no atributo admin do usuário autenticado.

🎯 Público-Alvo

Empresas e equipes que precisam de uma ferramenta interna para:

Analisar a performance de projetos ao longo do tempo

Gerenciar visualmente indicadores-chave de negócio (KPIs)

Controlar o acesso por nível de usuário

Trabalhar com dados tabulares sem necessidade de sistemas complexos