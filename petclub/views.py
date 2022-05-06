from django.shortcuts import render

# Create your views here.

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hola gente, estoy en el get!", status=200) # respuesta del servicio
    def patch(self, request):
        return Response (data="Hola gente, estoy en el patch!", status=200)   
    def delete(self, request):
        return Response (data="Hola gente, estoy en el delete!", status=200)
    def post(self, request):
        return Response (data="Hola gente, estoy en el post!", status=200)

class PetListAPIView(ListAPIView):
    def get(self, request):
        return Response(data="Hello, World !", status=200)

class PetAPIView(RetrieveAPIView):
    def get(self, request):
        return Response(data="Hello, World !", status=200)

class PersonView(APIView):
    def get(self, request):
        return Response(data="Hola gente, estoy en el get", status=200)
    def patch(self, request):
        return Response(data="Hola gente, estoy en el path", status=200)    
    def post(self, request):
        return Response(data="Hola gente, estoy en el post", status=200)
    def delete(self, request):
        return Response(data="Hola gente, estoy en el delete", status=200)

class PetView(APIView):
    def get(self, request):
        return Response(data="Hola gente, estoy en el get", status=200)
    def patch(self, request):
        return Response(data="Hola gente, estoy en el path", status=200)
    def post(self, request):
        return Response(data="Hola gente, estoy en el post", status=200)
    def delete(self, request):
        return Response(data="Hola gente, estoy en el delete", status=200)