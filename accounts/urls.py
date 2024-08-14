from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_user, name='logout'),
]
