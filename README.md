# TECH NEWS 👩🏽‍💻

## 📄 Sobre | About
<details>
  <summary>
    <strong>PT</strong>
  </summary>
   Raspagem do blog da Trybe para consultas de notícias sobre tecnologia

  🎯

    * Aplicar técnicas de raspagem de dados
    * Extrair dados de conteúdo HTML
    * Utilizar o terminal interativo do Python
    * Escrever módulos e importá-los
    * Armazenar os dados obtidos em um banco de dados
  <br>
</details>

<details>
  <summary>
    <strong>EN</strong>
  </summary>
  Trybe blog scraping for tech news queries

  🎯

    * Apply data scraping techniques
    * Extract data from HTML content
    * Use Python's interactive terminal
    * Write modules and import them
    * Store the obtained data in a database
  <br>
</details>
<br>

## 🛠️ Ferramentas | Tools
* [Python](https://www.python.org/)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)
<br>

 ## ⚒️ Como rodar a aplicação | How to run the application
<details>
  <summary> PT </summary> <br>

  Faça Download:
  ```
  git clone git@github.com:queite/tech-news.git
  ```
  Entre na pasta raiz:
  ```
  cd tech-news
  ```
  Crie um ambiente virtual:
  ```
  python3 -m venv .venv
  ```
  Ative o ambiente virtual:
  ```
  source .venv/bin/activate
  ```
  Instale as dependências:
  ```
  python3 -m pip install -r dev-requirements.txt
  ```
  Suba o container do banco de dados:
  ```
  docker-compose up -d mongodb
  ```
  Chame o script no terminal:
  ```
  tech-news-analyzer
  ```
  A partir dai escola primeiro a opção 0 para popular o banco de dados, em seguida é só testar as outras opções

</details>

<details>
  <summary> EN </summary> <br>

  Download the code:
  ```
  git clone git@github.com:queite/tech-news.git
  ```
  Enter the root folder:
  ```
  cd tech-news
  ```
  Create a virtual environment:
  ```
  python3 -m venv .venv
  ```
  Activate the virtual environment:
  ```
  source .venv/bin/activate
  ```
  Install dependencies:
  ```
  python3 -m pip install -r dev-requirements.txt
  ```
  Run the database container:
  ```
  docker-compose up -d mongodb
  ```
  Run the script on terminal:
  ```
  tech-news-analyzer
  ```
  From there choose the 0 option to populate the database, then test the other options
</details>
<br>

---
PT<br>
Projeto desenvolvido durante o módulo de ciências da computação na [Trybe](https://www.betrybe.com/).<br/>
Todos os projetos da [Trybe](https://www.betrybe.com/) usam `linters`, `Git` and `GitHub`.<br/>

EN<br>
Project developed in the Computer Science Module at the [Trybe](https://www.betrybe.com/) course.<br/>
All [Trybe](https://www.betrybe.com/) projects use `linters`, `Git` and `GitHub`.<br/>