"""ask_ekurakov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(\d+)$', views.question, name='question'),
    url(r'^hot/$', views.hot, name='hot'),
    url(r'^tag/(.*)$', views.tag, name='tag'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^create_article/$', views.create_article, name='create_article'),
    url(r'^create_answer/(\d+)$', views.create_answer, name='create_answer'),
]
