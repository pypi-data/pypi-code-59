from django.db import models

# Create your models here.

class doubt(models.Model):
    doubt = models.CharField(max_length=50)


class resolve(models.Model):
    doubt = models.ForeignKey(doubt, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
