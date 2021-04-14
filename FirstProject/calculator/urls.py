from django.urls import path

from calculator import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.addition, name = 'add'),
    path('sub', views.subtraction, name = 'sub'),
    path('multi', views.multiplication, name = 'multi'),
    path('div', views.division, name = 'div')
]



# whenever 'localhost:8000' will be called, function named 'index' will be 
# called that is present in views.py file, this will happen for all other routes
# as well