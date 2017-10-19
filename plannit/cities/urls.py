from django.conf.urls import include, url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^(?P<city_id>[0-9]+)/$',views.loadcity, name = "cities")
]
