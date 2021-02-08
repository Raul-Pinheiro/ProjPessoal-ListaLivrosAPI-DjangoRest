from rest_framework import viewsets
from rest_framework.views import exception_handler
from .models import Livros
from .serializers import LivrosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.
class LivrosViewSet(viewsets.ModelViewSet):
    """Exibe todos os livros desejados """
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
