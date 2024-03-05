from django.db import models
from django.db.models.deletion import CASCADE

# from datetime import date

# Create your models here.
class Elibrary(models.Model):
    Name = models.CharField(max_length=255)
    Subject = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Semester = models.PositiveIntegerField(default=0)
    Quantity = models.PositiveIntegerField(default=0)
    Price = models.PositiveIntegerField(default=0)

class EMember(models.Model):
    Name = models.CharField(max_length = 255)
    Semester = models.PositiveIntegerField(default = 0)
    Branch = models.CharField(max_length = 255)
    Mob_No = models.PositiveIntegerField(default = 0)


class ERecord(models.Model):
    Book_id = models.ForeignKey(Elibrary, on_delete=CASCADE)
    Member_id = models.ForeignKey(EMember, on_delete=CASCADE)
    issue_date = models.DateField()
    Return_date = models.DateField()
    Status = models.BooleanField(null=False)