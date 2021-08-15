from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="camionremorque"),
    path("modifierCamion", views.modifierCamion, name="modifierCamion"),
    path("loadMore/<str:name>", views.loadMore, name="loadMore"),
    
]