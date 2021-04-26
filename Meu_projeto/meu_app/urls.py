from django import path
from . import views

app_name = "meu_app"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    ##quando o usuario acessar usando a url não orientada a um slug
    # ela será enviada para a lista de post 
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
    ##quando a pessoa pesquisar corretamente por um slug ela será
    #levada a página desejada
]