from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_profile, name='create'),
    path('profile/', views.view_profile, name='profile'),
    path('update/<int:id>', views.update_profile, name='update'),
    path('delete/<int:id>', views.delete_profile, name='delete'),
]
