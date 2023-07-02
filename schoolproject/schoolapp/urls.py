from django.urls import path
from . import views

app_name='school'
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('form/',views.form,name='form'),
    path('getdata/',views.getdata,name='getdata'),
    path('confirm/',views.confirm,name='confirm'),
]
