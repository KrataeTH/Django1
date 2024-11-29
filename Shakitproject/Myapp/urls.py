# urls.py ของแอป
from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.main, name='main'),  # หน้าแสดงรายชื่อลูกค้า
    path('add/', views.add_customer, name='add_customer'),
    path('edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete/<int:pk>/', views.delete_customer, name='delete_customer'),
]
