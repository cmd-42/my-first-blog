from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model): #Post objects, Django object
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200) #title text at most 200 characters
	text = models.TextField() #unlimited text field for blog post contest
	created_date = models.DateTimeField(
		default=timezone.now)# date and time
	published_date = models.DateTimeField(
		blank=True, null=True) #date and time

	def publish(self): #void method to publish
		self.published_date = timezone.now()
		self.save()

	def __str__ (self): #method to return a string 
		return self.title
