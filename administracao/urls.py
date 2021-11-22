from django.urls import path
from .views import servicos_views, usuarios_views

urlpatterns = [
    path('servicos/cadastrar', servicos_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', servicos_views.listar_servicos, name='listar_servicos'),
    path('servicos/editar', servicos_views.editar_servico, name='editar_servico'),
    path('usuarios/cadastrar', usuarios_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', usuarios_views.listar_usuarios, name='listar_usuarios'),

]