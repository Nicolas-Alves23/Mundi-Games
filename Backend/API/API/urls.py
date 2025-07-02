from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path, include  # Importa funções para definir URLs e incluir outros arquivos de rotas

urlpatterns = [
    path("admin/", admin.site.urls),  # Rota para acessar o painel administrativo do Django (ex: /admin/)
    path('api/', include('app.urls'))  # Inclui as rotas definidas no arquivo 'urls.py' do app 'app', sob o prefixo /api/
]
