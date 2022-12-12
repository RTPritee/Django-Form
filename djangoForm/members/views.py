from django.http import HttpResponse
from django.shortcuts import redirect, render
from members.form import EmployeeForm
from .models import Employee

# Create your views here.


def index(request):
    # return HttpResponse("Hello world!")
    # return render(request,"index.html")
    return render(request, "index.html")


def show(request):
    members = Employee.objects.all()
    return render(request, "show.html", {'members': members})


def contact(request):
    print(">>>>>>>>>>>>>>>>>>")
    # temp = {}
    # print(request)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print("inside post")
        if form.is_valid():
            print("form is valid")
            try:
                form.save()
                print("form saved")
                # print(form)
                # return complain(request)
                return redirect('show')
            except:
                print("error")
    else:
        form = EmployeeForm()
        return render(request, 'index.html', {'form': form})


def complain(request):
    print("got it")
    return render(request, "complain.html")


def edit(request, id):
    members = Employee.objects.get(eid=id)
    return render(request, 'edit.html', {'members': members})


def update(request, id):
    members = Employee.objects.get(eid=id)
    form = EmployeeForm(request.POST, instance=members)
    print("inside update")
    if form.is_valid():
        print("form is updated")
        form.save()
        return redirect('show')
    return render(request, 'edit.html', {'members': members})


def delete(request, id):
    members = Employee.objects.get(eid=id)
    members.delete()
    return redirect('show')
