from . import views
from django.urls import path,include

urlpatterns = [
    path('main',views.main,name='main'),
    path('index',views.index,name='index'),
    path('',views.first,name='first' )

]