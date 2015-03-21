from django.db import models

# Create your models here.

class Salon(models.Model):	
	name = models.CharField(max_length=20)
	owner_name = models.CharField(max_length=30)
	address = models.CharField(max_length=100)


class Service(models.Model):
	title = models.CharField(max_length=30)
	content_text = models.CharField(max_length=300)
	salon = models.ForeignKey(Salon)
	price = models.IntegerField()


