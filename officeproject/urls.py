"""officeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.home,name='home'),
    path('signup/',views.SignUpView,name='signup'),
    url(r'^delete/(?P<username>[\w|\W.-]+)/$', views.delete_user, name='delete-user'),
    path('edit/<int:pk>/', views.update_user.as_view(), name='update-user'),
]
