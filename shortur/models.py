import random
import string

from django.db import models

# Create your models here.

def code_generator(size=8, chars= string.ascii_lowercase + string.ascii_uppercase + string.digits):
	# new_code = ''
	# for _ in range(size):
	# 	new_code = random.choice(chars)
	# return new_code
	return ''.join(random.choice(chars) for _ in range(size))


class MyUrl(models.Model):
	url 		= models.CharField(max_length=300)
	shortcode 	= models.CharField(max_length=18, unique=True)
	update		= models.DateTimeField(auto_now=True) 		#everytime model is saved
	timestamp	= models.DateTimeField(auto_now_add=True)	# when model was created
	
	def save(self, *args, **kwargs):
		print(" hii ")
		self.shortcode = code_generator()
		super(MyUrl, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)