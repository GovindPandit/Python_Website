from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    link = models.CharField(max_length=4000)
    photo = models.ImageField(upload_to="images/")
    pub_date = models.DateTimeField("Date Published")
