from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import *

NUMERO_MAXIMO_QUESTOES = 10


def index(request):
    if request.method == 'POST':
        try:
            tags = request.POST['tags']
            if (tags != ""):
                list = get_questions_with_tags(tags)
                return render(request, 'index.html', {"list": list})
            else:
                latest_list = Questao.objects.order_by('questao_data')[:20]
                return render(request, 'index.html', {"list": latest_list})
        except(KeyError):
            latest_list = Questao.objects.order_by('questao_data')[:20]
            return render(request, 'index.html', {"list": latest_list})
    else:
        latest_list = Questao.objects.order_by('questao_data')[:20]
        return render(request, 'index.html', {"list": latest_list})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def loginView(request):
    # metodo que verifica se existe dados em POST ( objetivo: minimalizar duas funcoes para uma funcao )
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            if (username == '' or password == ''):
                return render(request, 'login_form.html', {'error_message': 'Todos os campo não foram preenchidos'})
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('forum:index'))
                else:
                    return render(request, 'login_form.html', {'error_message': 'Username/Password inválidos'})
        except(KeyError):
            return render(request, 'login_form.html', {'error_message': 'Todos os campos não foram preenchidos'})
    else:
        return render(request, 'login_form.html', )


def sign_up(request):
    if request.method == 'POST':
        try:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            try:
                user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
                utilizador = Utilizador(user=user, imageURL="#", descricao="Sem Descrição.")
                utilizador.save()
                return HttpResponseRedirect(reverse("forum:loginView"))
            except:
                return render(request, "sign_up.html", {"error_message": "Erro ao criar o User. Tente Novamente"})
        except(KeyError):
            return render(request, "sign_up.html", {"error_message": "Erro"})
    else:
        return render(request, "sign_up.html")


@login_required(login_url='/forum/login')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:loginView'))


@login_required(login_url='/forum/login')
def profile(request):
    return render(request, 'profile.html')


# use in search-bar
def get_questions_with_tags(tags):
    questoes = {}
    for tag in tags.split():
        aux = Tag.objects.filter(tag_texto=tag)
        if aux:
            lista_questoes_com_tag = aux[0].questao.all()
            for questao in lista_questoes_com_tag:
                if questao in questoes.keys():
                    questoes[questao] = questoes[questao] + 1
                else:
                    questoes[questao] = 1
    tamanho = min(20, len(questoes))
    questoes_ordenadas = sorted(questoes.keys(), key=lambda k: questoes[k], reverse=True)[:tamanho]
    return list(questoes_ordenadas)


@login_required(login_url='/forum/login')
def editar_perfil(request):
    if request.method == 'POST':
        try:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            descricao = request.POST['descricao']
            upload_image(request)
            request.user.first_name = firstname
            request.user.last_name = lastname
            request.user.username = username
            request.user.password = password
            request.user.email = email
            request.user.utilizador.descricao = descricao
            request.user.save()
            request.user.utilizador.save()
            return HttpResponseRedirect(reverse('forum:profile'))
        except KeyError:
            return render(request, "editar_perfil.html", {'error_message': 'Erro: Tentar novamente'})
    else:
        return render(request, "editar_perfil.html")


def upload_image(request):
    if request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save("forum/static/images/" + request.user.username + ".png", myfile)
        uploaded_file_url = fs.url(filename)
        request.user.utilizador.imageURL = filename[6:]
        request.user.utilizador.save()
        return True
    return False


# @Graciano !!!! antes de chamar essa funcao, tem que verificar o utilizador se pode criar a questao(numero questoes < NUMERO_MAXIMO_QUESTOES)
@login_required(login_url='/forum/login')
def criar_questao(request):
    if request.method == 'POST':
        try:
            texto_questao = request.POST['textoquestao']
            tags = request.POST['tags']
            questao = Questao.objects.create(questao_texto=texto_questao, questao_data=timezone.now(),
                                             user=request.user)
            for tag in tags.split():
                aux = Tag.objects.filter(tag_texto=tag)
                if aux:
                    aux[0].questao.add(questao)
                else:
                    new_tag = Tag.objects.create(tag_texto=tag)
                    new_tag.questao.add(questao)
            if not request.user.is_superuser:
                request.user.utilizador.numeroQuestoes += 1
                request.user.utilizador.save()
        except(KeyError):
            return render(request, 'criar_questao.html', {'error_message': "Nem todos os campos foram escritos"})
        ##mandar para onde se der tudo certo?
        return HttpResponseRedirect(reverse('forum:profile'))
    else:
        return render(request, 'criar_questao.html')

@login_required(login_url='/forum/login')
def lista_questoes(request):
    questoes = Questao.objects.filter(user=request.user)
    return render(request,'lista_questoes.html',{'lista_questoes':questoes})

@login_required(login_url='/forum/login')
def alterar_questao(request,questao_id):
    questao = get_object_or_404(Questao,pk=questao_id) # obter questao, caso nao existe da erro 404
    if request.method == 'POST':
        # nao quero fazer agora
        return render(request, 'alterar_questao.html', {'questao': questao})
    else:
        return render(request,'alterar_questao.html',{'questao':questao})

# porque existe desse botao????
def tags(request):
    return render(request,'profile.html')

def detalhe_questao(request, questao_id):
    questao = get_object_or_404(Questao,pk=questao_id)
    render(request,'detalhe_questao.html',{'questao':questao})
