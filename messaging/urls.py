from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:receiver_id>/', views.chat, name='chat'),
]