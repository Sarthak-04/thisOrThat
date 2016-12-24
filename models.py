from django.db import models

# Create your models here.

class Record(models.Model):
	first_image_name = models.CharField(max_length=50)
	second_image_name = models.CharField(max_length=50)
	first_image_votes = models.PositiveIntegerField()
	second_image_votes = models.PositiveIntegerField()
	first_image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/image_one.jpg')
	second_image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/image_two.jpg')
	