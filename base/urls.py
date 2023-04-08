from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('add/<int:course_id>/', views.addcourse, name='add'),
    path('editGrade/<int:course_id>/', views.editGrade, name='editGrade'),
    path('remove/<int:course_id>/', views.removecourse, name='remove'),
    
]