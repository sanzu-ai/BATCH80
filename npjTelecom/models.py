from django.db import models

# Create your models here.
class Avenger(models.Model):
    name = models.CharField(max_length=50)
    add = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    email = models.EmailField()
    class Meta:
        db_table = 'avenger'
        
    def __str__(self) ->str:
        return self.name