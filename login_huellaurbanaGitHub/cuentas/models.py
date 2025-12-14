# models.py
from django.db import models
from django.contrib.auth.models import User

class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

class Comentario(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.pagina.titulo}'

# Create your models here.
