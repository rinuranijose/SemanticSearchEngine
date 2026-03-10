from django.db import models
from pgvector.django import VectorField

class Document(models.Model):

    title = models.CharField(max_length=500)
    content = models.TextField()

    embedding = VectorField(dimensions=768)

    def __str__(self):
        return self.title