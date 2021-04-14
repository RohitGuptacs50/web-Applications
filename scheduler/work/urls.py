from django.urls import path
from . import views




urlpatterns = [
    path('table/', views.work_table),
    path('insert_table/', views.insert_table, name='insert_in_table'),
    path('delete_table/<int:work_id>/', views.delete_table, name='delete_in_table'),
]