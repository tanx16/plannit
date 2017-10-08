from django.conf.urls import include, url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profiles/', include('profiles.urls'), name="profiles"),
]
