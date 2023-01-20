from django.db import models

# Create your models here.
class Career(models.Model):
 name = models.CharField(max_length=50)
 def __str__(self):
  return self.name

class Course(models.Model):
 code = models.CharField(max_length=20)
 name = models.CharField(max_length=50)
 credit_course = models.IntegerField()
 semester = models.CharField(max_length=10)
 clasroom = models.CharField(max_length=35)
 id_career = models.ForeignKey(Career, on_delete=models.CASCADE )
 
 class Meta:
  unique_together = ('code', 'id_career')
 def __str__(self):
  return self.name


class Day(models.Model):
 day_name = models.CharField(max_length=10)
 def __str__(self):
  return self.day_name


class Time(models.Model):
 cod_course = models.ForeignKey(Course, on_delete=models.CASCADE)
 cod_day = models.ForeignKey(Day, on_delete=models.CASCADE)
 open_t = models.IntegerField()
 close_t = models.IntegerField()

 class Meta:
  unique_together = ('cod_course', 'cod_day', 'open_t')

 def __str__(self):
  return str(self.cod_course) + "  " + str(self.cod_day)

class Button(models.Model):
 name = models.CharField(max_length=50)
 def __str__(self):
  return self.name