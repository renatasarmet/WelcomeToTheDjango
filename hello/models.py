from django.db import models

# Create your models here.
class Professor(models.Model):

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'

    def __str__(self):
        return 'Professor ' + self.nome + ' ' + self.sobrenome

    nome = models.CharField(max_length=50, verbose_name='nome')
    sobrenome = models.CharField(max_length=100, verbose_name='sobrenome')
    email = models.EmailField(verbose_name='e-mail')


class Materia(models.Model):

    class Meta:
        verbose_name = 'matéria'
        verbose_name_plural = 'matérias'

    def __str__(self):
        return 'Matéria ' + self.nome

    nome = models.CharField(max_length=100, verbose_name='nome')
    codigo = models.IntegerField(verbose_name='código')
    professor = models.ManyToManyField(Professor, verbose_name='professor(es)')
    descricao = models.TextField(verbose_name='descrição')

    TURMAS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    turma = models.CharField(max_length=1, choices=TURMAS)

