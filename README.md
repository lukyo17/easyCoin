# easyCoin
EasyCoin
Projeto criado por Daniel Sousa
Auxiliado por  Wilkinson Tavares


Projeto criado com finalidade de Merit Money
Utilizando Django com banco de dados PostgreSQL


- Requisitos

Python 3.+
Postgresql 10.+

- Instalação

Executar o arquivos de requerimentos através do comando.

"pip install -r requirements.txt"

*Caso apresente erro, deverá ser feito instalação manual dos recursos utilizados:

Django versão 3
"pip install django"

Django Extensions versão 2.2
"pip install django-extensions"

Psycopg2 versão 2.8 para integração com PostgreSQL
"pip install psycopg2"

Após isso será necessário ter um banco de dados criado com nome "easycoin".

Necessário rodar os seguintes comandos para criação da estrutura da aplicação

"python manage.py makemigrations"

Em seguida:

"python manage.py migrate"

Para validar se está tudo certo, iniciar a aplicação:

"python manage.py runserver"
