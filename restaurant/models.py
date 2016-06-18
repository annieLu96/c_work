from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50,blank = True)

	def __unicode__(self):
		return self.name

class Food(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=3,decimal_places = 0)
	comment = models.CharField(max_length=60,blank=True)
	is_spicy = models.BooleanField(default = False)
	restaurant = models.ForeignKey(Restaurant)

	def __unicode__(self):
		return self.name
# r4 = Food.objects.create(name  ='Strawberry Short Cake',price ='80',comment = 'today's specials',is_spicy = False,restaurant = sugar)