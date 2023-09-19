from django.shortcuts import render,redirect
from .models import Employee
from .form import Empform
# Create your views here.
def addemployee(request):
    empform = Empform()
    return render(request,'addemployee.html',{'empform':empform})

def addempdata(request):
    if request.method == 'POST':
        empform = Empform(request.POST)
        if empform.is_valid():
            empform.save()
            return redirect('empdetails')
        else:
            return render(request,'addemployee.html',{'empform':Empform()})
    else:    
        return render(request, 'addemployee.html')


def empdetails(request):
    emp=Employee.objects.all() 
    return render(request,'employeedetails.html',{'emp':emp})

def edit(request,eid):
    emps = Employee.objects.get(eid=eid)
    return render(request,'edit.html',{'emps':emps})

def update(request,eid):
    if request.method=="POST":
        emps=Employee.objects.get(eid=eid)
        form=Empform(request.POST,instance=emps)
        if form.is_valid():
            form.save()
            return redirect('empdetails')
        else:
            return render(request,'edit.html',{'emps':emps})
    return render(request,'edit.html',{'emps':emps})

def delete(request,eid):
    emps = Employee.objects.get(eid = eid)
    emps.delete()
    return redirect('empdetails')