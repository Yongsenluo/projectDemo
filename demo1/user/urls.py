from django.contrib.auth import views as authView
from django.urls import path
from .import views

app_name = 'user'

urlpatterns = [ 
    path('signup/', views.signupUser, name='signup'),
    path('login/', views.loginUser, name ='login'),
    path('logout/',  views.logoutUser, name ='logout'),
    path('userinformation/',views.userinformation,name ='userinformation')
]
