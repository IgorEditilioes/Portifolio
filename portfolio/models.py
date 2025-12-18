import uuid
from django.db import models
from django.utils.text import slugify

def upload_imagem_principal(instance, filename):
    ext = filename.split('.')[-1]
    nome_projeto = instance.slug
    return f'portfolio/{nome_projeto}/principal/{uuid.uuid4()}.{ext}'


def upload_imagem_secundaria(instance, filename):
    ext = filename.split('.')[-1]
    nome_projeto = instance.projeto.slug
    return f'portfolio/{nome_projeto}/secundarias/{uuid.uuid4()}.{ext}'

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.CharField(max_length=200)
    descricao_detalhada = models.TextField()
    tecnologias = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    imagem_principal = models.ImageField(
        upload_to=upload_imagem_principal
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    
class ImagemProjeto(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='imagens'
    )
    imagem = models.ImageField(
        upload_to=upload_imagem_secundaria
    )

    def __str__(self):
        return f'Imagem de {self.projeto.titulo}'
