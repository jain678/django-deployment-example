from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative_url,name = 'relative'),
    path('others/', views.others,name = 'others'),
]