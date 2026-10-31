from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/posts/', views.page_posts, name='page-posts'),
]
