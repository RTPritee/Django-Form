from django.http import HttpResponse
from django.shortcuts import redirect, render
from members.form import EmployeeForm 

# Create your views here.
def index(request):
    # return HttpResponse("Hello world!")
    # return render(request,"index.html")
    return render(request,"index.html")

def contact(request): 
    # print(">>>>>>>>>>>>>>>>>>")
    # temp = {}
    # print(request)
    if request.method == "POST":  
        form = EmployeeForm(request.POST) 
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        # print(form)
        # return complain(request)
        return redirect('complain')  

def complain(request):
    print("got it")
    return render(request,"complain.html")

