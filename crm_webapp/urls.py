from django.urls import path
from . import views


urlpatterns=[
    path("", views.home, name="home"),
    path("members", views.members, name="members"),
    path('details/<int:id>', views.details, name="details")
    # path("userdetails/<int:userId>", views.userdetails, name="userdetails"),
]