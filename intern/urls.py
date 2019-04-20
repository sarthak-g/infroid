from django.urls import path
from . import views
urlpatterns = [
    path('', views.InternView.as_view(), name='intern_list'),
    path('profile/create/', views.InternCreateView.as_view(), name ='intern_create'),
    path('profile/<int:pk>/edit/', views.InternUpdateView.as_view(), name='intern_edit'),
    path('profile/<int:pk>/delete/', views.InternDeleteView.as_view(), name='intern_delete'),
]
