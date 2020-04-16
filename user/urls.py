
from django.urls import path
from .api_views import  UserCreate 
from .serializers import LoginView
app_name = 'user'

urlpatterns = [
    path("signup/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),

]
