from rest_framework import viewsets
from lista_livros.models import Livros
from lista_livros.serializers import LivrosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.
class LivrosViewSet(viewsets.ModelViewSet):
    """Exibe todos os livros desejados """
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
