from django.db import models

# Create your models here.
class Add(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    author=models.CharField(max_length=20)
    description=models.TextField(max_length=100)
    
    def addit(self):
        self.save()