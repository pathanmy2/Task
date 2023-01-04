from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response

from App1.serializers import EmployeeSerializer
from rest_framework import status
from App1.models import Employee


@csrf_exempt
def employee_Register(request):
              
                                                        # Send Employee all details 
    if request.method == "POST":
        postData = json.loads(request.body)
        try:

            Employee.objects.get(email=postData["email"])
            return JsonResponse({"status": "failed", "description": "Record already exist"}, status=status.HTTP_502_BAD_GATEWAY)
        except:
            emp = Employee.objects.create(email=postData["email"], name=postData['name'], age=postData['age'], gender=postData['gender'], phone=postData['phone'],
                                          address=postData['address'], hno=postData['hno'], street=postData[
                'street'], city=postData['city'], state=postData['state'],
                companyName=postData['companyName'], fromDate=postData['fromDate'], toDate=postData['toDate'], qualificationName=postData['qualificationName'], percentage=postData['percentage'], titles=postData['titles'], description=postData['description'], photo=postData['photo'])

            expe = [{"companyName": postData['companyName'], "fromDate": postData['fromDate'],
                     "toDate": postData['toDate'], "address": postData['address']}]
            qualification = [{"qualificationName": postData['qualificationName'],
                              "fromDate": postData['from'], "toDate": postData['to'], "percentage": postData['percentage']}]
            emp.workExeperience = expe

            emp.address = [{"hno": postData['hno'], "street": postData['street'],
                            "city": postData['city'], "state": postData['state']}]

            emp.qualificiations = qualification

            emp.projects = [{"title": postData['titles'],
                             "description": postData['description']}]

            emp.save()

            return JsonResponse({"status": "success"}, status=status.HTTP_201_CREATED)


class Employee_Crud(APIView):
    def put(self, request, *args, **kwargs):
                  
                                                        # Edit using email id with including all the data
        postData = json.loads(request.body)
        try:
            emp = Employee.objects.get(email=postData["email"])
            emp.name = postData['name']
            emp.age = postData['age']
            emp.gender = postData['gender']
            emp.phone = postData['phone']
            emp.address = postData['address']
            emp.hno = postData['hno']
            emp.street = postData['street']
            emp.city = postData['city']
            emp.state = postData['state']
            emp.companyName = postData['companyName']
            emp.fromDate = postData['fromDate']
            emp.toDate = postData['toDate']
            emp.qualificationName = postData['qualificationName']
            emp.percentage = postData['percentage']
            emp.titles = postData['titles']
            emp.description = postData['description']
            emp.photo = postData['photo']

            expe = [{"companyName": postData['companyName'], "fromDate": postData['fromDate'],
                     "toDate": postData['toDate'], "address": postData['address']}]
            qualification = [{"qualificationName": postData['qualificationName'],
                              "fromDate": postData['from'], "toDate": postData['to'], "percentage": postData['percentage']}]
            emp.workExeperience = expe

            emp.address = [{"hno": postData['hno'], "street": postData['street'],
                            "city": postData['city'], "state": postData['state']}]

            emp.qualificiations = qualification

            emp.projects = [{"title": postData['titles'],
                             "description": postData['description']}]

            emp.save()
            return JsonResponse({"status": "success", "message": "updated"}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({"status": "failed", "description": "Record does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
                  
                                                        # Fetch using email id or fetch all the record
        try:
            if request.GET.get("email"):
                obj = Employee.objects.filter(
                    email=request.GET.get("email")).values()
            else:
                obj = Employee.objects.filter().values()
            return JsonResponse({"status": "success", "data": list(obj)}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status": "failed", "Exception": e}, status=status.HTTP_502_BAD_GATEWAY)

    def delete(self, request):
        obj = Employee.objects.filter(email=request.GET.get("email")).delete()
        return JsonResponse({"status": "success", "message": "deleted"}, status=status.HTTP_200_OK)

        
