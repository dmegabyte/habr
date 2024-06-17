
from django.urls import path
from . import views





urlpatterns = [
    path("", views.index, name="home"),
    path("room/<int:id>", views.room, name="view_room"),
    path("create_room", views.create_room, name="create_room"),

]
