from app.views import index, ClientViewSet, EmployeeViewSet
from django.urls import path 
from django.contrib import admin 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('clients/', ClientViewSet.as_view({'get': 'list'})),
    path('employees/', EmployeeViewSet.as_view({'get': 'list'})),
]