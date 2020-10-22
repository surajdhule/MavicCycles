from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.cycle_store, name='store'),
    path("detail/<int:myid>", views.cycle_details, name="cycledetails"),
    path('home/', views.cycle_store, name='cart'),

    ]