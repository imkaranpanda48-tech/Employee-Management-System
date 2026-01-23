from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path('', views.employee_list, name='list'),
    path('add/', views.employee_add, name='add'),
    path('<int:id>/', views.employee_detail, name='detail'),
    path('<int:id>/edit/', views.employee_edit, name='edit'),
    path('<int:id>/delete/', views.employee_delete, name='delete'),
]
