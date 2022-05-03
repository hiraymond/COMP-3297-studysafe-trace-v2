from django.urls import path
from . import views

urlpatterns = [
    path('venues/<str:hku_id>/<str:date>', views.view_venues),
    path('contacts/<str:hku_id>/<str:date>', views.view_contacts),
]