from django.shortcuts import render
from django.http import request,JsonResponse
from.models import employee

def employeedetails(request):
    if request.method == "GET":
        print("list of employee directory:" ,dir (employee.objects))
        obj = employee.objects.all()
        return JsonResponse({"response": list(obj.values("id","name"))})
    else:
        return render(request,"restpractice/templates")

# Create your views here.
