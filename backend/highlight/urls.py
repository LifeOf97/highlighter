from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'highlighter'

urlpatterns = [
    path('highlighter/api/', include([
        path('', views.APIRoot.as_view(), name='api-root'), # get
        path('highlight/', views.Highlighter.as_view(), name='highlight'), # post
        path('options/<str:option>/', views.Options.as_view(), name='highlight-options'), # get
    ])),
]

# urls can contain suffix patters like '.json', or not
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
