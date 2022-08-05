from django.urls import path
from . import views

app_name = 'highlighter'

urlpatterns = [
    path('', views.APIRoot.as_view(), name='api-root'), # get
    path('highlight/', views.Highlighter.as_view(), name='highlight'), # post
    path('options/<str:option>/', views.Options.as_view(), name='highlight-options'), # get
]
