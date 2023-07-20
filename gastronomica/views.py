from django.shortcuts import render
from django.http import JsonResponse
from gastronomica.models import Inscrito
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import InscritoSerializer
from rest_framework.decorators import api_view


def index(request):
    return render(request, 'index.html')


def guardar(request):
    emp = {
        'id':123,
        'nombre': 'Pedro',
        'email': 'pedro@gmail.com',
        'sueldo': 145555555
    }
    return JsonResponse(emp)

def verInscritos(request):
     inscritos= Inscrito.objects.all()
     data = { 'inscritos': list(inscritos.values()) }
     return JsonResponse(data)

@api_view(['GET', 'POST'])
def inscrito_list(request):
    if request.method == 'GET':
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detalle(request, id):
    try:
        inscrito = Inscrito.objects.get(pk=id)
    except Inscrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#CLASS BASED VIEW

class InscritoList(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = self.get_object(pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
