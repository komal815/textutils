"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index, name='index'),    #first ''-->what is at the end of url, http://127.0.0.1:8000
    #path('about',views.funcinabout, name='funcinabout'),   #http://127.0.0.1:8000/about
    #path('read',views.readfile, name='readfile'),
    #path('openlink',views.openlink1, name='openlink1'),
    #path('removepunc',views.removepunc, name='removepunc'),
    #path('capitalize',views.capitalizefirst, name='capitalizefirst'),
    #path('newlineremove',views.newlineremove, name='newlineremove'),
    #path('removespace',views.removespace, name='removespace'),
    #path('countcharacter',views.countcharacter, name='countcharacter'),
    #path('backchar',views.backchar, name='backchar'),
    path('template',views.template,name='template'),
    #path('template1',views.template1,name='template1'),
    path('analyze',views.analyze,name='analyze'),
    path('links',views.links,name='links')
    
    
]
