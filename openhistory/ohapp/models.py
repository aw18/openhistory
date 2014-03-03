from django.db import models

# Create your models here.
class Photos(models.Model):
    title = models.TextField()
    image_number = models.TextField()
    image_url = models.TextField()
    access_condition = models.TextField()
    branch_service = models.TextField()
    date_issued = models.TextField()
    description = models.TextField()
    location = models.TextField()
    photographer = models.TextField()
    subject = models.TextField()
