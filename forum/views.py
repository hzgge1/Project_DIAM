from datetime import timezone

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from forum.models import Questao, Resposta, Like, Utilizador, Tag


def index(request):
    latest_list = Questao.objects.order_by('questao_data')[:20]
    return render(request, 'index.html', {"list": latest_list})

def about(request):
    return render(request, 'about.html')

def loginView(request):
    # metodo que verifica se existe dados em POST ( objetivo: minimalizar duas funcoes para uma funcao )
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('forum:index'))
            else:
                return render(request, 'login_form.html', {'error_message': 'Username/Password inválidos'})
        except(KeyError):
            return render(request, 'login_form.html', {'error_message': 'Erro'})
    else:
        return render(request, 'login_form.html', )

@login_required(login_url='/forum/login')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:loginView'))
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
                utilizador = Utilizador(user=user, imageURL="images/default.png", descricao="Sem Descrição.")
                utilizador.save()
                return HttpResponseRedirect(reverse("forum:loginView"))
            except:
                return render(request, "sign_up.html", {"error_message": "Erro ao criar o User. Tente Novamente"})
        except(KeyError):
            return render(request, "sign_up.html", {"error_message": "Erro"})
    else:
        return render(request, "sign_up.html")

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
        filename = fs.save("images/" + request.user.username + ".png", myfile)
        uploaded_file_url = fs.url(filename)
        request.user.utilizador.imageURL = filename[6:]
        request.user.utilizador.save()
        return True
    return False

@login_required(login_url='/forum/login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/forum/login')
def criar_questao(request):
    if request.method == 'POST':
         try:
             texto_questao = request.POST['textoquestao']
             tags = request.POST['tags']
             questao = Questao.objects.create(questao_texto=texto_questao, questao_data=timezone.now(),user=request.user)
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
             return render(request, 'criar_questao.html', {'error_message': "Erro"})
         return HttpResponseRedirect(reverse('forum:index'))
    else:
        return render(request, 'criar_questao.html')



def pesquisa_questoes(request):
    if request.method == 'POST':
        try:
            tags = request.POST['tags']
            if (tags != ""):
                list = get_questions_with_tags(tags)
                return render(request, 'lista_questoes.html', {"list": list})
            else:
                return HttpResponseRedirect(reverse("forum:index"))
        except(KeyError):
            return HttpResponseRedirect(reverse("forum:index"))
    else:
        return HttpResponseRedirect(reverse("forum:index"))

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
def questoes_user(request):
    questoes = Questao.objects.filter(user=request.user)
    return render(request,'lista_questoes.html',{'lista_questoes':questoes})

def detalhe_questao(request, questao_id):
    questao = get_object_or_404(Questao,pk=questao_id)
    if request.method == 'POST':
        try:
            resposta_texto = request.POST['resposta_texto']
            Resposta.objects.create(questao=questao,user=request.user,resposta_texto=resposta_texto,resposta_data=timezone.now())
        except(KeyError):
            return render(request, "detalhe_qeustao.html", {'questao':questao, "erro_message":"Erro"})
    else:
        list_respostas = Resposta.objects.filter(questao=questao)
        render(request,'detalhe_questao.html',{'questao':questao,"list":list_respostas})

@login_required(login_url='/forum/login')
def apagar_questao(request, questao_id):
    questao = get_object_or_404(Questao,pk=questao_id)
    user = questao.user
    questao.delete()
    user.utilizador.numeroQuestoes -= 1
    user.utilizador.save()
    return HttpResponseRedirect(reverse("forum:index"))


@login_required(login_url='/forum/login')
def like_questao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        like = Like.objects.get(user=request.user, questao=questao)
        like.delete()
    except Like.DoesNotExist:
        Like.objects.create(user=request.user, questao=questao)
    return HttpResponseRedirect(reverse("forum:detalhe_questao", args=questao_id))
