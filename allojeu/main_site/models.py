from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jeux(models.Model):
    name = models.CharField(max_length=90)
    active = models.BooleanField(default=True)
    description = models.TextField(null = True)
    note = models.IntegerField(default=0)
    date = models.DateField(null = True)
    #avis = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    avis = models.TextField(null = True)
    note = models.IntegerField(null=True, default=None)
    jeux = models.ForeignKey('Jeux', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.author.username
    
class Recherche(models.Model):
    recherche = models.TextField(null = True)

    def __str__(self):
        return self.recherche

