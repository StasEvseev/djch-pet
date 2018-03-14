from django.urls import path

from chat.views import index, chat_view


urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', chat_view, name='chat')
]
