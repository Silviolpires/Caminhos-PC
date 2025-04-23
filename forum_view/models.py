from django.db import models

class Post(models.Model):
    TIPOS_CHOICES = [
        ('evento', 'Evento'),
        ('anuncios', 'Anúncio'),
    ]
   
    tipo = models.CharField(max_length=10, choices=TIPOS_CHOICES)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='uploads/', blank=True, null=True)
    likes = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titulo
