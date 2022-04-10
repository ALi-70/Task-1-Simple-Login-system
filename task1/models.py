from django.db import models

# Create your models here.
class doc_table(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	image = models.ImageField(upload_to = "images")

	username = models.CharField(max_length=40)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=40)
	confirm_password = models.CharField(max_length=40)
	address = models.CharField(max_length=100)


class pat_table(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	image = models.ImageField(upload_to = "images")

	username = models.CharField(max_length=40)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=40)
	confirm_password = models.CharField(max_length=40)
	address = models.CharField(max_length=100)