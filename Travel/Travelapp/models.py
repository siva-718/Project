from django.db import models

# Create your models here.
class place(models.Model):
    City=models.CharField(max_length=200)
    IMG=models.ImageField(upload_to='pics')
    Address=models.TextField()
    Bedroom=models.CharField(max_length=20,default='0')
    Bathroom=models.CharField(max_length=20,default='0')
    Area=models.CharField(max_length=20,default='0')
    Floor=models.CharField(max_length=20,default='0')
    def __str__(self):
        return self.City