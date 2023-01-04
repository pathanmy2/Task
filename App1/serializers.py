

from rest_framework import serializers
from App1.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
              class Meta:
                            model = Employee
                            fields = "__all__"

              # def create(self,validated_data):
              #               print(validated_data,"=====================")
              # #               # return Employee.objects.create(**validated_data)

              # def update(self, instance, validated_data, *args, **kwrgs):
              #               print(validated_data,"=============================================")
              #               for k, v in validated_data.items():
              #                             if k in instance.__dict__.keys():
              #                                           instance.__dict__[k] = v
                            
              #               instance.save()
              #               return instance