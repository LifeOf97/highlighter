from django.urls import path, include
from rest_framework import routers
from . import views

appname = 'highlight'

urlpatterns = [
    path('api/', include([
        path('highlighter/', views.Highlighter.as_view(), name='highliter'),
    ])),
]
