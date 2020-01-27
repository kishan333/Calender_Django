from django.urls import path
from . import views

urlpatterns = [
   
    # path('',views.index,name='index'),
    path('register/',views.register, name='register'),
    path('',views.user_login, name='login' ),
    path('addEvent/',views.addEvent, name='addEvent'),
    path('viewEvent/',views.viewEvent, name='viewEvent'),
]