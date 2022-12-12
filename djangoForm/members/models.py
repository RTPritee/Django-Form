from django.db import models
CALLTYPE_CHOICES = (
    ('Complain', 'Complain'),
    ('Assistance', 'Assistance'),
    ('Queries', 'Queries'),
    ('No response', 'No response')
)
COMPLAIN_CHOICES = (
    ('Early Marriage', 'Early Marriage'),
    ('Load Shedding', 'Load Shedding'),
    ('Eve Teasing', 'Eve Teasing',)
)
ASSISTENCE_CHOICES = (
    ('assist_1', 'assist_1'),
    ('assist_2', 'assist_2'),
    ('assist_3', 'assist_3'),
    ('assist_4', 'assist_4')
)
class Calltype(models.Model):
    id = models.AutoField(primary_key=True)
    dbcalltype = models.CharField(max_length=100, choices=CALLTYPE_CHOICES)

class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    dbmsisdn = models.CharField(max_length=15)
    dbname = models.CharField(max_length=100)
    dboccupation = models.CharField(max_length=100)
    # dbcalltype = models.ForeignKey(Calltype,null=True,on_delete=models.CASCADE)
    dbdate = models.DateField()
    dbdescription = models.TextField()
    
    class Meta:
        db_table = "members"

