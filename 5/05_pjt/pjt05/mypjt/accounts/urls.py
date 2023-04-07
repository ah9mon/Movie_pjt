from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('delete/', views.delete, name = 'delete'),
    path('update/', views.update, name = 'update'),
    path('password/', views.password, name = 'password'),
]