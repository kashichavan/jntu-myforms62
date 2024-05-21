from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registration
from .models import RegistrationModel
# Create your views here.

def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_Name')
        last_name=request.POST.get('last_Name')
        age=request.POST.get('age')
        email=request.POST.get('email')

        s=RegistrationModel(username=username,first_name=first_name,last_name=last_name,age=age,email=email)
        s.save()
        return HttpResponse("<h1>form is submitted</h1>")
    
    form=Registration()
    data={'form':form}
    return render(request,'reg.html',context=data)



