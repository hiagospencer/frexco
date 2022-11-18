from django.urls import path
from desafio_tech.views import cadastro, Homepage

app_name = 'desafio_tech'


urlpatterns = [
    
    path('', cadastro, name='cadastro'),
    path('homepage/', Homepage.as_view(), name='homepage'),
]