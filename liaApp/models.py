from django.db import models

# Create your models here.
from django.db import models
class Department(models.Model):
    dnumber = models.IntegerField(blank=True, null=True)
    dname = models.CharField(max_length=15, blank=True, null=True)
    mgr_ssn = models.CharField(max_length=9, blank=True, null=True)
    mgr_start_date = models.DateField(blank=True, null=True)

class Meta:
#managed = False
    db_table = 'department'
    
class Employee(models.Model):
    fname = models.CharField(max_length=8, blank=True, null=True)
    minit = models.CharField(max_length=2, blank=True, null=True)
    lname = models.CharField(max_length=8, blank=True, null=True)
    ssn = models.CharField(primary_key=True, max_length=9)
    bdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=27, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    salary = models.IntegerField()
    super_ssn = models.CharField(max_length=9, blank=True, null=True)
    dno = models.IntegerField()
    
class Meta:
        #managed = False
    db_table = 'employee'