from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    parent=models.ForeignKey(User,on_delete=models.CASCADE)
    child_id=models.IntegerField(primary_key=True)


    def __str__(self):
        return self.name