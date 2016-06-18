from django.shortcuts import render
from django.shortcuts import render_to_response
from restaurant.models import Restaurant,Food

#using python to create a mysql database, without learning any mysql 


# Create your views here.
def menu(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('menu.html',locals())

