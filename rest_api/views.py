from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from rest_api.serializers import AgendamentoModelSerializer

from reserva.models import Reserva

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]    




# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        nomeRecebido = request.data.get('nome')
        idadeRecebida = request.data.get('idade')
        return Response({ "message": f"Olá, {nomeRecebido}! Você tem {idadeRecebida} anos." })
    
    return Response({ 'message': 'Hello World!' })