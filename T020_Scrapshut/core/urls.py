from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('new_post/', views.PostCreate, name ='new_post')
]
