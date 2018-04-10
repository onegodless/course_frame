from django.db import models

class Attributes(models.Model):
	height = models.FloatField(default=0.0)
	weight = models.IntegerField(default=0)
	name = models.CharField(max_length=20, default="")

	def __str__(self):
		return self.name
