from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('homepage/',views.homepage, name="homepage"),
    path('signup/',views.signup, name="signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('todopage/', views.todopage, name="todopage"),
    path('edit_todo/<int:srno>', views.edit_todo, name="edit_todo"),
    path('delete_todo/<int:srno>', views.delete_todo, name="delete_todo"),
    path('signout', views.signout, name='signout')

]