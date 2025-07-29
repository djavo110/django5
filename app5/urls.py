from django.urls import path
from app5.views import *

urlpatterns = [
    path('', avtosalon, name="avtosalon"),
    path('brend/', brend, name="brend"),
    path('car/<int:pk>', view=car, name="car"),
    path('add_car/', view=add_car, name="add_car"),
]