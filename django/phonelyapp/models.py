from django.db import models

class Person(models.Model):
	phone_number = models.CharField(unique=True,primary_key=True,max_length=15)
	partner = models.ForeignKey('Person',blank=True,null=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1)
	age = models.IntegerField(default=1)
	interests = models.TextField()
	rating = models.IntegerField(default=5)
	safe_mode = models.BooleanField(default=True)
	def __unicode__(self):
		return self.phone_number
