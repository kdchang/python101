from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
	title = models.CharField(max_length=100)
	image_path = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)

	# def __unicode__(self):
	# 	return self.title