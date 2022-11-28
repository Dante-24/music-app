from django.urls import path
from .views import RoomView, CreateRoomView

urlpatterns = [
    path('home', RoomView.as_view()),
    path('create-room/', CreateRoomView.as_view()),
    # path('create-room/<int:pk>/', CreateRoomView.as_view())
]
