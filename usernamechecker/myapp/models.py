from django.db import models

# Create your models here.
class Userdata(models.Model):
    username= models.CharField( max_length=50)

    def __str__(self):
        return self.username
    