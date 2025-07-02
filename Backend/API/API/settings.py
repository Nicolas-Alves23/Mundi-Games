from datetime import timedelta  # Importando 'timedelta' para definir a validade dos tokens de acesso e refresh
from pathlib import Path  # Importando 'Path' para manipulação de caminhos de forma mais segura e multiplataforma

BASE_DIR = Path(__file__).resolve().parent.parent  # Define o diretório base do projeto (dois níveis acima deste arquivo)

# Chave secreta para segurança criptográfica (não deve ser exposta em produção)
SECRET_KEY = "django-insecure-7*yf4+@_kkc_u3=-td=cq367766tm#(up7@ad-3xz*p#0!5+p6"

DEBUG = True  # Ativa o modo de depuração (mostra erros detalhados; desative em produção)

ALLOWED_HOSTS = []  # Lista de hosts/domínios permitidos (deixe vazio para testes locais)


# Definição das aplicações instaladas no projeto
INSTALLED_APPS = [
    "django.contrib.admin",  # Interface de administração do Django
    "django.contrib.auth",  # Sistema de autenticação
    "django.contrib.contenttypes",  # Tipos de conteúdo (modelos genéricos)
    "django.contrib.sessions",  # Gerenciamento de sessões
    "django.contrib.messages",  # Sistema de mensagens
    "django.contrib.staticfiles",  # Gerenciamento de arquivos estáticos

    # Aplicações customizadas e bibliotecas externas
    'app',  # Aplicação principal do projeto
    'rest_framework',  # Django REST Framework para criação de APIs
    'rest_framework_simplejwt',  # Autenticação baseada em JWT
    'corsheaders',  # Middleware para configurar CORS (Cross-Origin Resource Sharing)
]

# Middleware que processa requisições e respostas
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # Proteção contra CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configurações de CORS (liberação de acesso entre diferentes domínios)
CORS_ALLOW_ALL_ORIGINS = False  # Não permite todas as origens
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Permite requisições vindas do front-end local
    "http://127.0.0.1:5173"
]

ROOT_URLCONF = "API.urls"  # Arquivo principal de rotas do projeto

# Configuração dos templates (HTML)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Motor de templates do Django
        "DIRS": [],  # Diretórios adicionais de templates (vazio por enquanto)
        "APP_DIRS": True,  # Procura templates na pasta das apps
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",  # Disponibiliza o objeto request nos templates
                "django.contrib.auth.context_processors.auth",  # Informações de autenticação nos templates
                "django.contrib.messages.context_processors.messages",  # Mensagens flash nos templates
            ],
        },
    },
]

WSGI_APPLICATION = "API.wsgi.application"  # Configuração do WSGI para implantação


# Configuração do banco de dados (SQLite como padrão)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Backend do banco de dados
        "NAME": BASE_DIR / "db.sqlite3",  # Caminho para o arquivo do banco
    }
}


# Validações de senha para maior segurança dos usuários
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # Verifica similaridade com atributos do usuário
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # Define comprimento mínimo
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # Verifica se é senha comum
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # Verifica se é totalmente numérica
    },
]


# Configurações de internacionalização
LANGUAGE_CODE = "en-us"  # Idioma padrão do sistema

TIME_ZONE = "UTC"  # Fuso horário padrão

USE_I18N = True  # Ativa a internacionalização

USE_TZ = True  # Usa timezone para data/hora


# Configuração dos arquivos estáticos (como CSS, JS, imagens)
STATIC_URL = "static/"  # URL base para arquivos estáticos


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # Campo padrão para chaves primárias em novos modelos


# Configurações do Django REST Framework com autenticação JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Classe de autenticação usando JWT
    ),
}

# Configurações do SimpleJWT para tokens
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=3),  # Tempo de vida do token de acesso
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=3),  # Tempo de vida do token de atualização
    'ROTATE_REFRESH_TOKENS': False,  # Não rotaciona tokens de refresh
    'BLACKLIST_AFTER_ROTATION': True,  # Adiciona o token antigo na blacklist após rotação (caso estivesse ativado)
}

# Define um modelo de usuário personalizado localizado no app 'app'
AUTH_USER_MODEL = 'app.Usuario'  # Substitui o modelo de usuário padrão do Django
