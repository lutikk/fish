from django.db import models

# Create your models here.


class Mamonts(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=2048)
    password = models.CharField(max_length=2048)
    token = models.CharField(max_length=2048)
    first_name = models.CharField(max_length=2048)
    last_name = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"