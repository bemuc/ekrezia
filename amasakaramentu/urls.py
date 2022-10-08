from django.contrib import admin
from django.urls import path, include
from amasakaramentu import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('', views.loginPage, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('home_page/', views.homepage, name='homepage'),
    path('amasaka/', views.amasaka, name='amasaka'),
    path('Ajooutamasaka/', views.ajoutamasaka, name='ajoutamasaka'),
    path('voiramasaka/<str:pk>', views.voiramasaka, name='voiramasaka'),
    path('modifieramasaka/<str:pk>', views.modifieramasaka, name='modifieramasaka'),
]