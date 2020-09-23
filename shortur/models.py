from django.db import models
from django.conf import settings

# Create your models here.

from .utils import code_generator, create_shortcode

# ModelManager :: handles stuffs related to the model 
# eg: objects.all(), objects.filter()


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class MyUrlManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super(MyUrlManager, self).all(*args, **kwargs)
		qs = qs.filter(active=True)
		return qs

	def refresh_shortcodes(self, items= None):
		qs = MyUrl.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs = qs.order_by('id')[:items]
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes += 1
		return "New Codes made:: {i}".format(i=new_codes)



class MyUrl(models.Model):
	url 		= models.CharField(max_length=300)
	shortcode 	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	update		= models.DateTimeField(auto_now=True) 		#everytime model is saved
	timestamp	= models.DateTimeField(auto_now_add=True)	# when model was created
	active 		= models.BooleanField(default=True)

	objects = MyUrlManager()
	some_random = MyUrlManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode()
		super(MyUrl, self).save(*args, **kwargs)

	# class Meta:
	# 	ordering = '-id'

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)