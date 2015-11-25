from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateField()
	class Meta:
		db_table = 'users'

class Weapon(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	damage = models.IntegerField()
	users = models.ManyToManyField(User)
	class Meta:
		db_table = 'weapons'