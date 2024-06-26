from django.urls import path

from .views import index, create_employee
from django.contrib import admin


urlpatterns = [
    path('', index, name="client_index"),
    path('create_employee', create_employee, name="create_employee"),
    path('admin/', admin.site.urls),
]