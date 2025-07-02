import os  # Importa o módulo 'os' para trabalhar com variáveis de ambiente

from django.core.asgi import get_asgi_application  # Importa a função que retorna a aplicação ASGI do Django

# Define a variável de ambiente com o caminho para o módulo de configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "API.settings")

# Cria a aplicação ASGI que será usada por servidores assíncronos (como Daphne, Uvicorn) para servir o projeto
application = get_asgi_application()
 