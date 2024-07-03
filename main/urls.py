
from django.urls import path
from . import views
from . import auth_views





urlpatterns = [
    path("", views.index, name="home"),
    path("room/<int:id>/", views.room, name="view_room"),
    path("create_room/", views.create_room, name="create_room"),

    #
    path("login/", auth_views.login_page, name="login"),
    path("register/", auth_views.register_page, name="register"),
    path("logout/", auth_views.logout_page, name="logout"),


]
