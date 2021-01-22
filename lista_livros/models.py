from django.db import models

# Create your models here.

class Livros(models.Model): 
    titulo_livro = models.CharField(max_length=100)
    autor_livro = models.CharField(max_length=20)
    editora_livro = models.CharField(max_length=20)
    # valor_livro = models.CharField(max_length=10, blank=True, null=True)
    valor_livro = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

