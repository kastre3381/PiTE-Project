from django.db import models
from beer_db.models import Beer

# Create your models here.

class PreferenceSnippet(models.Model):

	ABV_value = models.IntegerField()

	predicted_beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

	
	Style_Key = models.IntegerField()
	Ave_Rating = models.IntegerField()
	Min_IBU = models.IntegerField()
	Max_IBU = models.IntegerField()
	Astringency = models.IntegerField()
	Body = models.IntegerField()
	Alcohol = models.IntegerField()
	Bitter = models.IntegerField()
	Sweet = models.IntegerField()
	Sour = models.IntegerField()
	Salty = models.IntegerField()
	Fruits = models.IntegerField()
	Hoppy = models.IntegerField()
	Spices = models.IntegerField()
	Malty = models.IntegerField()
	Average_IBU = models.IntegerField()