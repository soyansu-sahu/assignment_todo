from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length = 100)
    Description = models.TextField()
    category_choices = [
        ("Indoor",'indoor'),
        ("Outdoor",'outdoor')
    ]
    Category = models.CharField(max_length=100,choices = category_choices)

    Create_date = models.DateTimeField(auto_now_add = True)
    Complete_date = models.DateTimeField()


    def __str__(self):
        return self.Name