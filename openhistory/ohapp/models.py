from django.db import models

# Create your models here.
class Photos(models.Model):
    mikan_number = models.IntegerField()
    title = models.CharField(max_length=500)
    image_number = models.CharField(max_length=30)
    image_url = models.URLField(max_length=200)
    access_condition = models.CharField(max_length=1000)
    branch_service = models.CharField(max_length=1000)
    date_issued = models.DateTimeField()
    description = models.TextField()
    location = models.CharField()
    photographer = models.CharField()
    subject = models.CharField()