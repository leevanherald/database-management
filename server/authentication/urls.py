from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name='login'),
    # path('members/details/<int:id>', views.details, name='details'),
    path('register/', views.register, name="register"),
]