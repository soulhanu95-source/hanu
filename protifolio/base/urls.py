from django.urls import path
from . import views
urlpatterns = [
    path('',views.base1,name='base1'),
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('extra/',views.extra,name='extra'),
    path('project/',views.project,name='project'),
    
]
