from django.urls import path, include
from .views import *


urlpatterns = [
    path('group/', index, name='index'),
    path('page/',include('app_page.urls') ),
]
