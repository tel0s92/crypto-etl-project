.Tema do Projeto
Análise histórica de criptomoedas utilizando processo ETL e dashboard interativo.


.Definição da Base de Dados
Foi utilizado uma Base de Dados de preços de criptomoedas obtidas na plataforma kaggle contendo
informações sobre cotação, datas, preços e volume negociados em várias criptomoedas.
Abrangendo históricos de período de 2010 até Maio de 2026;
O objetivo é obter informações verídicas sobre as varias informações de preço e volume do mercado de criptomoedas
afim de traçar comparativos e obter informações específicas.


.Divisão de Tarefas e Atribuições dos Membros/Colaboradores da Equipe:
Marcelo Cesar Milagres Ferreira -Líder do projeto e desenvolvedor principal.

Rehael de Holanda Henriques - Pesquisa e validação dos datasets.

Gilson Ferreira de Lima - Auxiliar de tratamento e padronização dos dados.

Ian Manoel Almeida do Vale - Análise exploratória de dados.

Daniel Nascimento de Araujo - Documentação e organização do projeto.

Fabio Roberto Soares Filho - Suporte ao dashboard e experiência visual.

Vinicius Viana Pedrosa - Testes e validação do sistema.



.Objetivo da Análise
O objetivo deste projeto é realizar um processo completo de ETL (Extract, Transform, Load) utilizando dados históricos de criptomoedas obtidos através da plataforma Kaggle.
A análise busca identificar comportamentos históricos das criptomoedas, permitindo visualizar:
- O valor dos preços das criptomoedas;
- volume negociado;
- máximas e mínimas históricas;
- Filtragem por dia específicos

Além disso, o projeto tem como finalidade aplicar conceitos de:
- ciência de dados;
- tratamento de dados com Pandas;
- armazenamento em banco de dados;
- visualização de dados com dashboard Streamlit.

---

.Planejamento das Tarefas
 1. Coleta dos Dados
- Escolha do dataset no Kaggle;
- Download dos arquivos CSV;
- Organização da estrutura do projeto.

2. Processo ETL
---> Extract
- Leitura automática dos arquivos CSV utilizando Python e Pandas.

---> Transform
- Tratamento dos dados;
- Conversão de datas;
- Remoção de valores nulos;
- Padronização das colunas;
- Consolidação dos datasets.

---> Load
- Armazenamento dos dados tratados em:
  - CSV processado;
  - banco de dados SQLite.

 3. Desenvolvimento do Dashboard
- Construção de dashboard interativo utilizando Streamlit;
- Criação de filtros e gráficos;
- Exibição de métricas financeiras.

 4. Publicação do Projeto
- Organização do repositório;
- Criação da documentação;
- Publicação no GitHub.

---

.Ideia Inicial do Dashboard
O dashboard foi planejado para apresentar informações históricas sobre criptomoedas de forma visual e interativa.

A proposta inclui:
- filtro por criptomoeda;
- filtro por período;
- gráfico histórico de preços;
- gráfico de volume negociado;
- visualização completa dos dados.

O objetivo é facilitar a análise visual do comportamento das criptomoedas ao longo do tempo.

---