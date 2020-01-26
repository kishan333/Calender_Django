from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]