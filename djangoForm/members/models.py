from django.db import models

# Create your models here.
class Employee(models.Model):  
    msisdn = models.CharField(max_length=15) 
    name = models.CharField(max_length=100) 
    
    class Meta:  
        db_table = "members"  