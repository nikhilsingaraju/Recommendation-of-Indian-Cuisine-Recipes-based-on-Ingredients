"""Indiancuisinerecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from Indiancuisinerecipes.views import index, customer, managerloginaction, managerlogin, logout, customerdetailspage, \
    managerbase, activatecustomer, foodcourt, foodcourtdetailspage, activatefoodcourt, addrecipes, managerhome, \
    viewitems
from customer.views import customerloginaction, customerregistration, ingredients, ingredientsanalysis, customerpage, \
    downloaditems, recommend, recommended, foodcolor,  recipes ,getfoodcolor
from foodcourt.views import foodcourtloginaction, foodcourtregistration, items, murgmakhani, RoganJosh, MalaiKofta, \
    PapdiChaat, Dhokla, Chole, PalakPaneer, Naan, Alugobi, KaaliDaal, findingredients, foodcourtpage, additems, \
    sendrecipes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^logout/',logout, name="logout"),
    url(r'^managerbase/',managerbase,"managerbase"),
    url(r'^managerhome/',managerhome,name="managerhome"),
    url(r'^customer/',customer, name="customer"),
    url(r'^customerpage/',customerpage,name="customerpage"),
    url(r'^customerloginaction/',customerloginaction, name="customerloginaction"),
    url(r'^customerregistration/',customerregistration, name="customerregistration"),
    url(r'^customerdetailspage/',customerdetailspage, name="customerdetailspage"),
    url(r'^managerlogin/',managerlogin, name="managerlogin"),
    url(r'^managerloginaction/',managerloginaction, name="managerloginaction"),
    url(r'^activatecustomer/',activatecustomer, name="activatecustomer"),
    url(r'^foodcourt/',foodcourt, name="foodcourt"),
    url(r'^foodcourtpage/',foodcourtpage, name="foodcourtpage"),
    url(r'^foodcourtloginaction/',foodcourtloginaction,name="foodcourtloginaction"),
    url(r'^foodcourtregistration/',foodcourtregistration, name="foodcourtregistration"),
    url(r'^foodcourtdetailspage/',foodcourtdetailspage, name="foodcourtdetailspage"),
    url(r'^activatefoodcourt/',activatefoodcourt,name="activatefoodcourt"),
    url(r'^items/',items, name="items"),
    url(r'^murgmakhani/',murgmakhani, name="murgmakhani"),
    url(r'^RoganJosh',RoganJosh,name="RoganJosh"),
    url(r'^MalaiKofta/',MalaiKofta, name="MalaiKofta"),
    url(r'^PapdiChaat/',PapdiChaat, name="PapdiChaat"),
    url(r'^Dhokla/',Dhokla, name="Dhokla"),
    url(r'^Chole/',Chole,name="Chole"),
    url(r'^PalakPaneer/',PalakPaneer, name="PalakPaneer"),
    url(r'^Naan',Naan, name="Naan"),
    url(r'^Alugobi/',Alugobi,name="Alugobi"),
    url(r'^KaaliDaal/',KaaliDaal, name="KaaliDaal"),
    url(r'^addrecipes/',addrecipes, name="addrecipes"),
    url(r'^ingredients/',ingredients, name="ingredients"),
    url(r'^ingredientsanalysis/',ingredientsanalysis, name="ingredientsanalysis"),
    url(r'^findingredients/',findingredients, name="findingredients"),
    url(r'^additems/',additems, name="additems"),
    url(r'^downloaditems/',downloaditems, name="downloaditems"),
    url(r'^viewitems/',viewitems, name="viewitems"),
    url(r'^recommend/',recommend, name="recommend"),
    url(r'^recommended/',recommended, name="recommended"),
    url(r'^sendrecipes/',sendrecipes, name="sendrecipes"),
    #url(r'^foodcourtrecipe/',foodcourtrecipe, name="foodcourtrecipe"),
    url(r'^foodcolor/',foodcolor, name="foodcolor"),
    #url(r'^detect/',detect, name="detect"),
    url(r'^recipes/',recipes,name="recipes"),
    url(r'^getfoodcolor/',getfoodcolor,name='getfoodcolor'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)