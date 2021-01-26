from django.db import models

# Create your models here.

class Task(models.Model):
    
    taskName= models.CharField(max_length=50)
    complete=models.BooleanField(default=False)
    dateAdded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskName
    
