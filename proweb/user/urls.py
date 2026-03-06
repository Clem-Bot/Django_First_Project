from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.login_users, name="login_users"),
    path('logout/', views.logout_users, name = 'logout_users'),
    path('register/', views.register_users, name = 'register_users')
]