from django.db import models

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

class User(models.Model):
	role = models.CharField(max_length=10)
	nick = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=30)
	email = models.EmailField()
	def __str__(self):
		return self.nick

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
