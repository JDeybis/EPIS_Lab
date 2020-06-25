from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import home, login, create_users

urlpatterns = [
    path('', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='login/login.html'), name='logout'),
    path('home/', home, name='home'),

    path('create_users', create_users, name='create_users')
]
