from django.urls import include, path
from . import views

app_name = 'forum'
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),

    path("login", views.loginView, name="loginView"),
    path("logout", views.logoutView, name="logoutView"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("editar_perfil", views.editar_perfil, name='editar_perfil'),

    path("profile", views.profile, name="profile"),
    path("criar_questao", views.criar_questao, name="criar_questao"),
    path("pesquisa_questoes", views.pesquisa_questoes, name="pesquisa_questoes"),
    path("questoes_user", views.questoes_user, name="questoes_user"),

    path("<int:questao_id>/detalhe_questao", views.detalhe_questao, name='detalhe_questao'),
    path("<int:questao_id>/apagar_questao", views.apagar_questao, name='apagar_questao'),
    path("<int:questao_id>/like_questao", views.like_questao, name='like_questao'),
]