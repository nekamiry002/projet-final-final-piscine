from django.db import models

# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    email = models.EmailField()
    content = models.TextField(null = True)
    
    def __str__(self):
        return self.title