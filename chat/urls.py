from django.urls import path

from . import views

urlpatterns = [
    path('', views.direct_chat, name='direct-chat'),
    path('<str:room_name>/', views.room, name='room'),
]
