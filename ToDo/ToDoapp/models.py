from django.db import models

# Create your models here.
class TODO(models.Model):
    Task = models.CharField(max_length=200)
    Priority = models.IntegerField()
    Date=models.DateField()

    def __str__(self):
        return self.Task