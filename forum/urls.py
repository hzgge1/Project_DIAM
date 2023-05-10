from django.urls import include, path
from . import views

app_name = 'forum'
urlpatterns = [
    path("", views.index, name="index"), # pagina inicial/home
    path("about", views.about, name="about"), # pagina about

    path("login", views.loginView, name="loginView"), # pagina login / funcao login -> pagina index
    path("logout", views.logoutView, name="logoutView"), # funcao logout -> pagina index
    path("sign_up", views.sign_up, name="sign_up"), # pagina signup / funcao registar -> pagina login
    path("editar_perfil", views.editar_perfil, name='editar_perfil'), # pagina editar perfil / funcao editar perfil -> pagina perfil

    path("profile", views.profile, name="profile"), # pagina perfil
    path("criar_questao", views.criar_questao, name="criar_questao"), # pagina criar questao / funcao criar questao -> pagina index
    path("pesquisa_questoes", views.pesquisa_questoes, name="pesquisa_questoes"), # funcao pesquisa questoes -> pagina lista questoes
    path("questoes_user", views.questoes_user, name="questoes_user"), # funcao questoes user -> pagina lista questoes

    path("<int:questao_id>/detalhe_questao", views.detalhe_questao, name='detalhe_questao'), # pagina detalhe questao
    path("<int:questao_id>/apagar_questao", views.apagar_questao, name='apagar_questao'), # funcao apagar questao
    path("<int:questao_id>/like_questao", views.like_questao, name='like_questao'), # funcao da like a questao
]