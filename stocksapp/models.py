from django.db import models

# Create your models here.
class Stocks(models.Model):
	ticker = models.CharField(max_length=15)

	def __str__(self):
		return self.ticker
