from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.verse_list, name='verse_list'),
]