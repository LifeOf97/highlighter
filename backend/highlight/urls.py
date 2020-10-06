from django.urls import path, include
from rest_framework import routers
from . import views

appname = 'highlight'

# router = routers.SimpleRouter()
# router.register(r'highlighter', views.Highlighter, basename='highlighter')

urlpatterns = [
    path('api/', include([
        path('highlighter/', views.Highlighter.as_view(), name='highliter'),
    ])),
]
