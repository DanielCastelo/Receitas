from django.urls import path

from . import views #arquivo "views" faz a manipulação de qual url vamos manipular e exibir para o usuario

urlpatterns = [ #urlpatterns define o mapeamento entre URLs e Views
    path('', views.index, name='index' ), #primeiro parametro = rota, segundo parametro = index, terceiro parametro = namespace
    path('<int:receita_id>', views.receita, name='receita' )
]