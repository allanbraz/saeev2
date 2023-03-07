"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app.views import home,store,dologin,logouts,changePassword,detalhes, dashboard,EdificacoesList, EdificacoesCreate,\
    EdificacoesUpdate, delete_ambientes, edificacoes_delete, EdificacoesDetailView

app_name = 'edificacoes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('store/', store),
    path('dologin/', dologin),
    path('logouts/', logouts),
    path('password/', changePassword, name='password'),
    path('index/', detalhes, name='index'),
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('register/', TemplateView.as_view(template_name="register.html")),
    path('dashboard/', dashboard, name='dashboard'),
    path('edificacoes/', EdificacoesList.as_view(), name='list_edificacoes'),
    path('createe/', EdificacoesCreate.as_view(), name='create_edificacoes'),
    path('update_edificacoes/<int:pk>/', EdificacoesUpdate.as_view(), name='update_edificacoes'),
    path('detail_edificacoes/<int:pk>/', EdificacoesDetailView.as_view(), name='detail_edificacoes'),
    path('delete-ambientes/<int:pk>/', delete_ambientes, name='delete_ambientes'),
    path('edificacoes/delete/<int:pk>/', edificacoes_delete, name='edificacoes_delete'),
    path('newlg/', TemplateView.as_view(template_name="newlg.html"),name='newlg'),

]