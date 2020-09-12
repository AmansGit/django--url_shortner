from django.db import models

# Create your models here.
class MyUrl(models.Model):
	url = models.CharField(max_length=300)
	shortcode = models.CharField(max_length=18, unique=True)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)