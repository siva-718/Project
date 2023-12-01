from django.db import models

# Create your models here.
class Movie(models.Model):
    Name=models.CharField(max_length=250)
    Desc=models.TextField()
    Year=models.IntegerField()
    Img=models.ImageField(upload_to='gallary')
    def __str__(self):
        return self.Name