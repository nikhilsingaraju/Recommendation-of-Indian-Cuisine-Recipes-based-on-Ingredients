from random import randint

from django.contrib import messages
from django.shortcuts import render

from customer.models import customerregistrationmodel
from foodcourt.models import foodcourtregistrationmodel, addrecipemodel


def index(request):
    context = {}
    return render(request, "index.html", context)

def customer(request):
    return render(request,"customer/customer.html", )

def foodcourt(request):
    return render(request,"foodcourt/foodcourt.html")

def managerlogin(request):
    return render(request,'manager/managerlogin.html')

def managerloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            print(usid)
            pswd = request.POST.get('password')
            if usid == 'Manager' and pswd == 'Manager':
                return render(request, 'manager/managerhome.html')
            else:
                messages.success(request, 'Invalid user id and password')
    return render(request, 'manager/managerlogin.html')

def managerbase(request):
    context = {}
    return render(request, 'managerbase.html',context)

def managerhome(request):
    return render(request, 'manager/managerhome.html')

def logout(request):
    return render(request,'index.html')

def customerdetailspage(request):
    managerdata = customerregistrationmodel.objects.all()
    return render(request,'manager/viewcustomerdata.html',{'object':managerdata})

def activatecustomer(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        customerregistrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        customerdata = customerregistrationmodel.objects.all()
        return render(request,'manager/viewcustomerdata.html',{'object':customerdata})

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def foodcourtdetailspage(request):
    foodcourtdata = foodcourtregistrationmodel.objects.all()
    return render(request,'manager/viewfoodcourtdata.html',{'object':foodcourtdata})

def activatefoodcourt(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        foodcourtregistrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        foodcourtdata = foodcourtregistrationmodel.objects.all()
        return render(request,'manager/viewfoodcourtdata.html',{'object':foodcourtdata})


def addrecipes(request):
    return render(request,'index.html')

def viewitems(request):
    viewitem = addrecipemodel.objects.all()
    return render(request, 'manager/viewitems.html', {'object': viewitem})

