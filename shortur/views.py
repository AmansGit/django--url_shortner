from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def myurl_redirect_view(request, shortcode, *args, **kwargs):
	# print(request.user)
	# print(request.user.is_authenticated)
	print(shortcode)
	print(kwargs)
	return HttpResponse("function based view")

class MyUrlRedirectView(View):
	def get(self, request, shortcode, *args, **kwargs):
		return HttpResponse("Class based view")