from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Salon(models.Model):	
	name = models.CharField(max_length=20)
	owner_name = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	


class Service(models.Model):
	title = models.CharField(max_length=30)
	content_text = models.CharField(max_length=300)
	salon = models.ForeignKey(Salon)
	price = models.FloatField()
	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)


class Reservation(models.Model):	
	user = models.ForeignKey(User)
	service = models.ForeignKey(Service)
	date = models.DateField()
	time = models.TimeField()
	

class Comments(models.Model):
	user = models.ForeignKey(User)	
	service = models.ForeignKey(Service)
	date = models.DateField()
	content_text = models.CharField(max_length=300)
