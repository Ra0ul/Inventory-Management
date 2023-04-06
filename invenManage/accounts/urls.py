from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    # path('sign-in/', views.user_login, name='sign-in'),
    # path('logout/', views.user_logout, name='logout'),
]
