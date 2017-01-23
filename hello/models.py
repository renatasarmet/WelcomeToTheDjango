from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(models.Model):

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'

    def __str__(self):
        x = 'Professor' if self.sexo == 'M' else 'Professora'
        return x + ' ' + self.nome + ' ' + self.sobrenome

    nome = models.CharField(max_length=50, verbose_name='nome')
    sobrenome = models.CharField(max_length=100, verbose_name='sobrenome')
    email = models.EmailField(verbose_name='e-mail')

    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    sexo = models.CharField(max_length=1, verbose_name='sexo', choices=SEXO, default='F')


class Sala(models.Model):

    class Meta:
        verbose_name = 'sala'
        verbose_name_plural = 'salas'

    def __str__(self):
        return 'Sala ' + self.numero_sala

    numero_sala = models.CharField(max_length=4, verbose_name='sala')
    departamento = models.CharField(max_length=50, verbose_name='departamento')




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
    sala = models.ForeignKey(Sala, null=True, blank=True, verbose_name='sala')

    TURMAS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    turma = models.CharField(max_length=1, choices=TURMAS)

class Curso(models.Model):
    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return 'Curso ' + self.nome_curso

    nome_curso = models.CharField(max_length=100, verbose_name='curso')
    coordenador = models.ForeignKey(Professor, verbose_name='coordenador')
    duracao_semestres = models.IntegerField(verbose_name='duração em semestres')



class Aluno(models.Model):
    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        # (self.sexo == 'M' ? 'Aluno' : 'Aluna'
        x = 'Aluno' if self.sexo == 'M' else 'Aluna'
        return x + ' ' + self.user.first_name + ' ' + self.user.last_name

    user = models.OneToOneField(User)
    RA = models.IntegerField(verbose_name='registro acadêmico', unique=True)
    curso = models.ForeignKey(Curso, verbose_name='curso')

    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    sexo = models.CharField(max_length=1, verbose_name='sexo', choices=SEXO, default= 'F')