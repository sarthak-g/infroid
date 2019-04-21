from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.InternView.as_view(), name='intern_list'),
    path('profile/create/', views.InternCreateView.as_view(), name ='intern_create'),
    path('profile/<int:pk>/edit/', views.InternUpdateView.as_view(), name='intern_edit'),
    path('profile/<int:pk>/delete/', views.InternDeleteView.as_view(), name='intern_delete'),
    path('particular/', views.ParticularRecordView, name='particular_record'),
    path('particular/<int:pk>/edit/', views.ParticularUpdateView.as_view(), name='particular_edit'),
    path('active/', views.ActiveIntern, name='active_intern'),

]
