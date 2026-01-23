from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employees/employee_list.html", {"employees": employees})

def employee_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("employees:list")
    else:
        form = EmployeeForm()
    return render(request, "employees/employee_form.html", {"form": form})

def employee_edit(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=emp)
        if form.is_valid():
            form.save()
            return redirect("employees:list")
    else:
        form = EmployeeForm(instance=emp)
    return render(request, "employees/employee_form.html", {"form": form})

def employee_delete(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        emp.delete()
        return redirect("employees:list")
    return render(request, "employees/employee_confirm_delete.html", {"emp": emp})

def employee_detail(request, id):
    emp = get_object_or_404(Employee, id=id)
    return render(request, "employees/employee_detail.html", {"emp": emp})



