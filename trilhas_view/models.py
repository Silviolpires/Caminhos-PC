from django.db import models
from home_view.models import PessoaFisica

class Trilha(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    distancia = models.DecimalField(max_digits=5, decimal_places=2, help_text="Distância em quilômetros")
    duracao = models.DurationField(help_text="Duração estimada (formato: HH:MM:SS)")
    nivel_dificuldade = models.CharField(
        max_length=20,
        choices=[
            ('facil', 'Fácil'),
            ('moderado', 'Moderado'),
            ('dificil', 'Difícil'),
            ('muito_dificil', 'Muito Difícil')
        ]
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    guias = models.ManyToManyField(PessoaFisica, related_name='trilhas_guiadas')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'
        ordering = ['nome']