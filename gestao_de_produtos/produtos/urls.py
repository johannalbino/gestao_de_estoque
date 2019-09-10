from django.urls import path
from .views import index
from .views import novo
from .views import editar
from .views import excluir

urlpatterns = [
    path('', index, name='index'),
    path('novoProduto', novo, name='novo'),
    path('editar/<int:id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
]