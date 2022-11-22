from django.db import models

# # models.py
# class Hotel(models.Model):
# 	name = models.CharField(max_length=50)
# 	img = models.ImageField(upload_to='')

class Hotel(models.Model):
    name= models.CharField(max_length=500)
    img= models.FileField(upload_to='')

    def __str__(self):
        return self.name + ": " + str(self.videofile)