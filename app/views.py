from django.db import connection
from django.http import HttpResponse
from presidio_analyzer import AnalyzerEngine, RecognizerResult
from presidio_anonymizer import AnonymizerEngine, OperatorConfig

# drf get view
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from client_app.models import Employee

from .models import Client


def index(request):
    return HttpResponse("<h1>Public Index</h1>")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()
    phone_num_text = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = "__all__"

    # def get_values(self, dictionary):
    #     text_to_anonymize = "His name is Mr. Jones and his phone number is 212-555-5555"
    #     # %%
    #     analyzer = AnalyzerEngine()
    #     analyzer_results = analyzer.analyze(text=text_to_anonymize, entities=["PHONE_NUMBER"], language='en')
    #
    #     print(analyzer_results)

    def get_extra_data(self, obj):
        anonymizer = AnonymizerEngine()

        some_magic_key = "WmZq4t7w!z%C&F)J"

        text = "My name is James Bond farzi admi"

        anonymized_text = anonymizer.anonymize(
            text=text,
            analyzer_results=[
                RecognizerResult(
                    entity_type="PERSON",
                    start=0,
                    end=len(text),
                    score=0.8,
                ),
            ],
            operators={"PERSON": OperatorConfig("encrypt", {"key": some_magic_key})},
        )

        return anonymized_text.text

    def get_phone_num_text(self, obj):
        analyzer = AnalyzerEngine()
        text = "His name is Mr. Jones and his phone number is 212-555-5555"
        analyzer_results = analyzer.analyze(
            text=text,
            entities=["PHONE_NUMBER"],
            language="en",
        )

        anonymizer = AnonymizerEngine()

        anonymized_text = anonymizer.anonymize(
            text=text,
            analyzer_results=analyzer_results,
        )

        return anonymized_text.text


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(self.request.tenant)
        bigco = Client.objects.get(name="bigco")
        connection.set_tenant(bigco)
        return Employee.objects.all()

    def get_object(self):
        return self.queryset.filter(client=self.request.client)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
