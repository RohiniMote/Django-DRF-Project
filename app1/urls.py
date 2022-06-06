from django.urls import path
from app1.views import LaptopView,ShowLaptopView,UpdateLaptopView,deleteLaptopView

urlpatterns=[
    path('lv/',LaptopView,name='addLaptop_url'),
    path('slap/',ShowLaptopView,name='showlaptop_url'),
    path('up/<int:id>/',UpdateLaptopView,name='updatelaptop_url'),
    path('dl/<int:id>/',deleteLaptopView,name='deletelaptop_url'),

]