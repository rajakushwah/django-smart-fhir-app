from . import views
from django.urls import path,include

urlpatterns = [
    path('home',views.home,name='home' ),
    path('',views.main,name='main' )

]