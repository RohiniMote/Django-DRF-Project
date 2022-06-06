from django.urls import path
from authapp.views import registerView,loginView,logoutView,twostepView


urlpatterns=[
    path('reg/',registerView,name='register_url'),
    path('log/',loginView,name='login_url'),
    path('logout',logoutView,name='logout_url'),
    path('verify/',twostepView,name='verify')
]