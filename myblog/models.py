from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPosts(models.Model):
	title		=	models.CharField(max_length=250)
	short_des	=	models.CharField(max_length=250)
	description	=	models.TextField()
	create_date	=	models.DateTimeField(default = timezone.now)

class Comments(models.Model):
	name	=	models.CharField(max_length=50)
	email	=	models.CharField(max_length=100)
	comment =	models.TextField()
	date 	=	models.DateTimeField(default=timezone.now)
	postid	=	models.ForeignKey(BlogPosts, on_delete=models.CASCADE)