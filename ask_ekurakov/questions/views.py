from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from questions.models import Article, Comment, Tag, UserProfile#####
from django.http import Http404
from django.http import JsonResponse, HttpResponseRedirect
from questions.forms import *
from questions import models#####
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


#{{form.as_p}}


def index(request):
    questions = Article.objects.published()
    return render(request, 'templates/index.html', {'questions' : questions})

def question(request, num):
    question = get_object_or_404(Article, id=num)
    articles = Comment.objects.fromArticle(num)
    answerForm = CommentForm()
    return render(request, 'templates/question.html', {'articles' : articles, 'question' : question, 'form' : answerForm})

def hot(request):
    questions = Article.objects.best_published()
    return render(request, 'templates/hot.html', {'questions' : questions})

def tag(request, tag):
    try:
        articles = Article.objects.with_tag(tag)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'templates/tag.html',{'articles' : articles})

@login_required
def ask(request):
    return render(request, 'templates/ask.html')


@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            curLogin = form.cleaned_data['login']
            curPassword = form.cleaned_data['password']
            user = authenticate(username = curLogin, password = curPassword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        
    return render(request, 'templates/login.html', {'form' : LoginForm()})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # save new author
            newUser = User(
                        username = form.cleaned_data['login'],
                       )
            newUser.set_password(form.cleaned_data['password'])
            newUser.save()
            UserProfile(
                user= newUser,
                username=form.cleaned_data['username'],
                avatar = form.cleaned_data['avatar']
            ).save()
            
            
            return HttpResponseRedirect("/")
    else:
        form = UserForm()
    return render(request,'templates/signup.html', {'form':form})


@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            #article = form.save()
            article = Article(
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                author = UserProfile.objects.get(user_id=request.user.id),
            )
            article.save()
            tags = form.cleaned_data['tags'].split(',')
            for t in tags:
                try:
                    tag = Tag.objects.get(name=t)
                except ObjectDoesNotExist:
                    tag = Tag(name=t)
                    tag.save()
                article.tags.add(tag)
            return HttpResponseRedirect(reverse('question', args=[article.id]))
    else:
        form = ArticleForm()
    return render(request,"templates/create_article.html", {"form" : form})

@login_required
def create_answer(request, qid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                text = form.cleaned_data['text'],
                published_by = UserProfile.objects.get(user_id=request.user.id),
                article = get_object_or_404(Article, id=qid)
            )
            comment.save()
            return HttpResponseRedirect(str(reverse('question', args=[qid])) + '#%d'%comment.id)
    else:
        form = ArticleForm()
    return render(request,"templates/create_answer.html", {"form" : form})

@login_required
def like(request):
    article_id = request.POST.get('article_id')
    if not article_id:
        return JsonResponse({'status':'error'})

## Add to urls path to here
    try:
        article = models.Article.objects.get()
    except DoesNotExist:
        return JsonResponse(DoesNotExist)
##   
    article = Article.objects.get(pk=article_id)
    article.rating += 1
    article.save()


#def post_list_all(request):
#        articles =  Article.objects.published()
#        limit = 10

#def paginate(request, qs):
#                try:
#                    limit = int(request.GET.get('limit', 10))
#                except ValueError:
#                    limit = 10
#                if limit > 100:
#                    limit = 10
#                try:
#                    page = int(request.GET.get('page', 1))
#                except ValueError:
#                    raise Http404
#                paginator = Paginator(qs, limit)
#                try:
#                    page = paginator.page(page)
#                except EmptyPage:
#                    page = paginator.page(paginator.num_pages)
#                return page

