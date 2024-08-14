from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_user, name='logout'),
]

# Ajouter la configuration pour servir les fichiers statiques pendant le développement
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )