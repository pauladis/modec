from django.db import models

class Vessel(models.Model):
    code = models.CharField(max_length=7, primary_key=True, unique=True, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.code