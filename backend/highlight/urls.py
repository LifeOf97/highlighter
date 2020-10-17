from django.urls import path, include
from rest_framework import routers
from . import views

appname = 'highlight'

urlpatterns = [
    path('api/', include([
        path('options/<str:option>/', views.Options.as_view(), name='highlight-options'),
        path('highlighter/', views.Highlighter.as_view(), name='highlighter'),
    ])),
]
