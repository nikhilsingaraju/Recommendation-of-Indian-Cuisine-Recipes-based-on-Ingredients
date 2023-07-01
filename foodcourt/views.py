from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse

# Create your views here.
from customer.forms import customeringredientsform
from customer.models import customeringredientsmodel
from foodcourt.forms import foodcourtregistrationform, addrecipeForm
from foodcourt.models import foodcourtregistrationmodel


def foodcourtpage(request):
    return render(request,'foodcourt/foodcourtpage.html')

def foodcourtregistration(request):
    if request.method == 'POST':
        form = foodcourtregistrationform(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'you are successfully registred')
            return HttpResponseRedirect('foodcourt/foodcourt.html')
        else:
            print('Invalid')
    else:
        form = foodcourtregistrationform()
    return render(request,"foodcourt/foodcourtregistration.html",{'form':form})



def foodcourtloginaction(request):
    if request.method == "POST":
        usid = request.POST.get('loginid')
        print(usid)
        pswd = request.POST.get('password')
        print(pswd)
        try:
            check = foodcourtregistrationmodel.objects.get(loginid=usid, password=pswd)
            request.session['id'] = check.loginid
            #request.session['loggedteacher'] = check.name
            status = check.status
            print("user  id ",check.loginid)
            if status == "activated":
               #request.session['stuid'] = check.loginid
               request.session['email'] = check.email
               return render(request,'foodcourt/foodcourtpage.html')
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request,'foodcourt/foodcourt.html')

            return render(request,'foodcourt/foodcourtpage.html')
        except Exception as e:
            print('Exception is ',str(e))
    messages.success(request, 'Invalid Login Details')
    return render(request,'foodcourt/foodcourt.html')

def items(request):
        return render(request, "foodcourt/items.html", )

def murgmakhani(request):
    return render(request,"foodcourt/murgmakhani.html")

def RoganJosh(request):
    return render(request,"foodcourt/RoganJosh.html")

def MalaiKofta(request):
    return render(request,"foodcourt/MalaiKofta.html")

def PapdiChaat(request):
    return render(request,"foodcourt/PapdiChaat.html")

def Dhokla(request):
    return render(request,"foodcourt/Dhokla.html")

def Chole(request):
    return render(request,"foodcourt/Chole.html")

def PalakPaneer(request):
    return render(request,"foodcourt/PalakPaneer.html")

def Naan(request):
    return render(request,"foodcourt/Naan.html")

def Alugobi(request):
    return render(request,"foodcourt/Alugobi.html")

def KaaliDaal(request):
    return render(request,"foodcourt/KaaliDaal.html")

def findingredients(request):
    customeringredients = customeringredientsmodel.objects.all()
    return render(request, 'foodcourt/findingredients.html',{'object':customeringredients})

def additems(request):
    if request.method == 'POST':
        form = addrecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('foodcourt/additems_list.html')
    else:
        form = addrecipeForm()
    return render(request, 'foodcourt/additems.html', {'form': form})

def sendrecipes(request):
        if request.method == 'GET':
            id = request.GET.get('id')
            print('Food Receipe ID is = ',id)
            customeringredientsmodel.objects.filter(id=id).update(status='sent')
            customeringredients = customeringredientsmodel.objects.all()
            return render(request, 'foodcourt/findingredients.html', {'object': customeringredients})


