from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MainImages(models.Model):
    imageid = models.CharField(max_length=100,db_column='ImageId')  # Field name made lowercase.
    id = models.CharField(max_length=100,primary_key=True)
    imageurl = models.CharField(max_length=100,db_column='imageUrl')  # Field name made lowercase.
    imagetype = models.CharField(max_length=100)
    postedby = models.CharField(max_length=100,db_column='postedBy')  # Field name made lowercase.
    restaurantid = models.CharField(max_length=100,db_column='restaurantId')  # Field name made lowercase.
    userid = models.CharField(max_length=100,db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_images'