from django.db import models
import jsonfield
# Create your models here.
class Employee(models.Model):
              name                        =             models.CharField(max_length=150,blank=True,null=True)
              email                       =             models.CharField(max_length=150,blank=True,null=True)
              age                         =             models.IntegerField(default=0)
              gender                      =             models.CharField(max_length=150,blank=True,null=True)
              phone                       =             models.CharField(max_length=150,blank=True,null=True)
              address                     =             jsonfield.JSONField(max_length=10000, blank=True, null=True)
              hno                         =             models.CharField(max_length=150,blank=True,null=True)
              street                      =             models.CharField(max_length=150,blank=True,null=True)
              city                        =             models.CharField(max_length=150,blank=True,null=True)
              state                       =             models.CharField(max_length=150,blank=True,null=True)
              workExeperience             =             jsonfield.JSONField(max_length=10000, blank=True, null=True)
              companyName                 =             models.CharField(max_length=150,blank=True,null=True)
              fromDate                    =             models.CharField(max_length=150,blank=True,null=True)
              toDate                      =             models.CharField(max_length=150,blank=True,null=True)
              qualificiations             =             jsonfield.JSONField(max_length=10000, blank=True, null=True)
              qualificationName           =             models.CharField(max_length=150,blank=True,null=True)
              percentage                  =             models.FloatField(default=0.0)
              projects                    =             jsonfield.JSONField(max_length=10000, blank=True, null=True)
              titles                      =             models.CharField(max_length=150,blank=True,null=True)
              description                 =             models.CharField(max_length=150,blank=True,null=True)
              photo                       =             models.FileField()
              
              def __str__(self) :
                      return self.name
        
