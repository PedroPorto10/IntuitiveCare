Este repositório contém um projeto que integra operações de banco de dados, uma API desenvolvida em Python e funcionalidades de web scraping e processamento de dados.

## Estrutura do Projeto

- **webScraping & dataProcessing**: Inclui scripts para web scraping e processamento de dados.
- **pythonAPI**: Contém a API desenvolvida em Python responsável por coletar os dados do arquivo "Relatorio_cadop.csv" e exibí-los dentro de uma página web escrita em Vue.js.
- **database**: Diretório responsável por criar as tabelas "operadoras" e "demonstracoes_contabeis", inserir os dados de arquivos .csv nas tabelas corretas (através do comando COPY) e fazer consultas na tabela "demonstracoes_contabeis".



## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Vue.js**: Utilizado possivelmente para a interface do usuário.
- **SQL**: Utilizado para estruturar e preencher as tabelas do banco de dados PostgreSQL.
