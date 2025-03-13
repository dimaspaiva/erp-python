# Sistema ERP

Essa é a base para a construção do sistema ERP, faça um fork e adicione as funcionalidades de acordo com o padrão estabelecido.

Para a execução de qualquer comando é recomendado estar com o `pyenv` ativo, para isso basta executar `.venv\Scripts\activate` no terminal.

## Instalação:

Ao iniciar execute os seguintes passos:

1. `py -3 -m venv .venv`;
2. `.venv\Scripts\activate`;
3. `pip install -r requirements.txt`/

## Inicialização do servidor:

Para inciar o servidor execute os seguintes comandos:

1. `.venv\Scripts\activate`;
2. `flask run`.

## Instalação de novas dependências

Para instalar novas depêndencias é necessário estar com o `pyenv` ativo e atualizar a lista de dependências que fica no arquivo `requirements.txt`, siga os passos:

1. `.venv\Scripts\activate`;
2. `pip install NOME_DA_BIBLIOTECA`;
3. `pip freeze > requirements.txt`.

## Modelos do banco de dados

Para adicionar um novo modelo no banco de dados, basta criar um novo arquivo dentro da pasta `models` e realizar a importação do arquivo dentro do arquivo `__init__.py` dentro da pasta models, como já é feito com o modelo Paciente.

## Rotas

Para adicionar um nova rota o processo é similar ao dos modelos, cria-se um arquivo da nova rota e adicionar a importação do mesmo dentro do arquivo `__init__.py` da pasta rotas.
