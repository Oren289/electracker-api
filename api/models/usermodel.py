from django.db import models

class User(models.Model):
   user_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=100)
   lorong_id = models.IntegerField()
   major_id = models.IntegerField()
   phone = models.CharField(max_length=20)

   def __str__(self):
      return self.name

