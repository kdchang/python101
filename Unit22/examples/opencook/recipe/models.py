from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
	id = models.CharField(primary_key=True, max_length=10000000)
	title = models.CharField(max_length=100)
	image_path = models.CharField(max_length=100)
	description = models.TextField()
	integrent = models.TextField()
	step = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.title