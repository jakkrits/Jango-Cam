from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('detection_hardcode/', views.detection_hardcode, name='detection_hardcode'),
    path('streaming/', views.streaming, name='streaming')
]