from django.urls import path, include
from . import views

appname = 'highlight'

urlpatterns = [
    path('api/', include([
        path('', views.Home, name='home-page'),
    ])),
]
