from django.db import models

class Mark(models.Model):
   name = models.CharField(max_length=30)


   def __str__(self):
       return self.name

class Color(models.Model):
   color = models.CharField(max_length=30)

   def __str__(self):
       return self.color


class Car(models.Model):
   mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
   model = models.CharField(max_length=30)
   price = models.IntegerField()
   color = models.ForeignKey(Color, on_delete=models.PROTECT)
   



