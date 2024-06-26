from django.db import connection
from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.response import Response

from client_app.models import Employee


def index(request):
    return HttpResponse("<h1>Public Index</h1>")


# drf get view

from rest_framework import viewsets, serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(self.request.tenant)
        bigco = Client.objects.get(name='smallco')
        connection.set_tenant(bigco)
        return Employee.objects.all()

    def get_object(self):
        return self.queryset.filter(client=self.request.client)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
