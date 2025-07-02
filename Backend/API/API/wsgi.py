import os  # Importa o módulo 'os' para interagir com variáveis de ambiente do sistema operacional

from django.core.wsgi import get_wsgi_application  # Importa a função que retorna a aplicação WSGI do Django

# Define a variável de ambiente que aponta para o módulo de configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "API.settings")

# Cria a aplicação WSGI que será usada por servidores (como Gunicorn, uWSGI, etc.) para servir o projeto
application = get_wsgi_application()
