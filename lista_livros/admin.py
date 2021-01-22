from django.contrib import admin

# Register your models here.
from lista_livros.models import Livros

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id','titulo_livro')



admin.site.register(Livros,LivrosAdmin)