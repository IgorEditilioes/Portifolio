from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.CharField(max_length=200)
    descricao_detalhada = models.TextField()
    tecnologias = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    imagem_principal = CloudinaryField(
        'imagem_principal',
        folder='portfolio/principal'
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

    imagem = CloudinaryField(
        'imagem_secundaria',
        folder='portfolio/secundarias'
    )

    def __str__(self):
        return f'Imagem de {self.projeto.titulo}'
