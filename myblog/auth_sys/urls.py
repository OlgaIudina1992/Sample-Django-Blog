from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    path('auth_sys/', UserRegisterView.as_view(), name='register')
    
]
