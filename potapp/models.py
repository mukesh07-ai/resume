from django.db import models




class portfolio(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    


# Create your models here.
