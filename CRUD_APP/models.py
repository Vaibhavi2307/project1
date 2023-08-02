from django.db import models


class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    eaddr=models.TextField()
    
