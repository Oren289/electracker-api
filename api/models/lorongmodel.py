from django.db import models

class Lorong(models.Model):
   lorong_name = models.CharField(max_length=10)

   def __str__(self):
      return self.lorong_name