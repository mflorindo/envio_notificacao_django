# Sistema Dispatcher

## Este sistema consiste em um gerenciador de envios de mensagens por três canais: Web Push, Email e SMS!

### Tecnologias/Frameworks:
Foi utilizado para este fim o framework Django/Python e como frontend o Bootstrap 4.
Para o Django foi utilizado a versão do **python 3.8**

### Instalação do projeto:

* Para que a instalação não atrapalhe o ambiente atual de sua máquina (você já poderá estar usando outra versão do python), recomendo fortemente a instalação do virtualenv. Basta seguir este [documento](http://devfuria.com.br/linux/instalando-virtualenv/).
* Após instalação e ativação do virtualenv, entre na pasta do sistema e execute pip3 install requirements.txt
* Crie as tabelas: **python manage.py migrate**
* Crie o superuser: **python manage.py createsuperuser**
* Execute a aplicação: **python manage.py runserver**
* Acesse o sistema no endereço padrão: **http://127.0.0.1:8000**

## Agora é só testar!

