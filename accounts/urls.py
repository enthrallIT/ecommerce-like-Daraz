from django.urls import path
from .views import register, login, forgot_password, user_logout

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),  
    path('forgot-password/', forgot_password, name='forgot_password'),
]
