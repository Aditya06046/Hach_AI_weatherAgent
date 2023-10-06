from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('',views.registerUser),
    path('login/',views.loginUser),
    path('logout/',views.logoutUser),
    path('home/',views.homePage),
]