from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponse
# Create your views here.
def add_employee(request):
    if request.method == 'GET':
        frm=EmployeeForm()
        return render(request, 'add_emp.html',{'form':frm})
    elif request.method == 'POST':
        frm=EmployeeForm(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponse('Employee Added Successfully')
        else:
            return render(request, 'add_emp.html',{'form':frm, 'refill':'try again'})