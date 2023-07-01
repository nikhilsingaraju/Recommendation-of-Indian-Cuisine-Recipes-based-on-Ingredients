from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from PIL import Image
from django.conf import settings

# Create your views here.
from nltk.corpus import wordnet

from customer.forms import customerregistrationform, recommendform
from customer.models import customerregistrationmodel, customeringredientsmodel, recommendmodel
from foodcourt.models import addrecipemodel

import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os
import os.path

def customerpage(request):
    return render(request,'customer/customerpage.html')


def customerregistration(request):
    if request.method == 'POST':
        form = customerregistrationform(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'you are successfully registred')
            return HttpResponseRedirect('customer/customer.html')
        else:
            print('Invalid')
    else:
        form = customerregistrationform()
    return render(request,"customer/customerregistration.html",{'form':form})


def customerloginaction(request):
    if request.method == "POST":
        usid = request.POST.get('loginid')
        print(usid)
        pswd = request.POST.get('password')
        print(pswd)
        try:
            check = customerregistrationmodel.objects.get(loginid=usid, password=pswd)
            request.session['customerid'] = check.loginid
            request.session['email'] = check.email
            #request.session['loggedteacher'] = check.name
            status = check.status
            print("customer  id ",check.loginid)
            if status == "activated":
               #request.session['stuid'] = check.loginid
               request.session['email'] = check.email
               return render(request,'customer/customerpage.html')
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request,'customer/customer.html')

            return render(request,'customer/customerpage.html')
        except Exception as e:
            print('Exception is ',str(e))
    messages.success(request, 'Invalid Login Details')
    return render(request,'customer/customer.html')


class NaiveBayes:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

known_recipes = [
    NaiveBayes('Aloogobi', set("Cauliflower|potatoes|turmeric|garammasala|curryleaves".split("|"))),
    NaiveBayes('Biryani', set("Rice|vegetables|butter|garlic|ginger".split("|"))),
    NaiveBayes('Carrothalwa', set("Carrot|Milk|Ghee|Cashew".split("|"))),
    NaiveBayes('Kheer', set("Rice|Milk|dry fruits|Ghee".split("|"))),
    NaiveBayes('Samosa', set("Potatoes|onions|peas|coriander|tamatoo".split("|"))),
    NaiveBayes('Chicken65', set("Chicken|onion|ginger|garlic|greenchilli|redchillipowder|turmeric|garammasala".split("|"))),
    NaiveBayes('Fish', set("Fish|ginger&garlic|greenchilli|redchillipowder".split("|"))),
    NaiveBayes('Kadaipaneer', set("Paneer|greenpeppers|tomato".split("|"))),
    NaiveBayes('Butterchicken', set("onion|garlic|ginger|butter|chicken|tomatopuree".split("|"))),
    NaiveBayes('Kheer', set("Rice|milk|dry fruits".split("|"))),
    NaiveBayes('Aloomethi', set("Potato|Methileaves".split("|"))),
    NaiveBayes('Avial', set("Coconutpaste|curd|vegetables|spices".split("|"))),
    NaiveBayes('Eggomelette', set("Egg|oil|greenchilli|onions".split("|"))),
    NaiveBayes('Koottu', set("Vegetable|daal|lentil|water".split("|"))),
    NaiveBayes('Rasam', set("tamarind|tomatoes|pepper".split("|"))),

]

def ingredients(request):
    return render(request,"customer/sendingredients.html")


def ingredientsanalysis(request):
    if request.method == "POST":
        ingredients = request.POST.get('ingredients')
        print(ingredients)
        usid = request.POST.get('loginid')
        print(usid)
        try:
            check = customerregistrationmodel.objects.get(loginid=usid)
            usid = check.loginid
            email = check.email
            storingredients = ingredients
            #print( check.email, ingredients)
            ingredients = ingredients.lower()
            ingredients = ingredients.split(",")
            possible = []
            for ingredient in ingredients:
                for recipe in known_recipes:
                    if ingredient in recipe.ingredients:
                        possible.append(recipe.name)
            if possible:
                for x in possible:
                    print('recipe is = ',x)
                    ing = wordnet.synsets(x)
                    description = ''
                    if len(ing)!=0:
                        description = ing[0].definition()
                        print(description)
                    else:
                        description = 'No Data found'
                        customeringredientsmodel.objects.create(loginid=usid,email=email,ingredients=storingredients,recipes=x,descriptions=description)
                        #messages.success(request,'no data found')
            else:
                messages.success(request, "Good news! You're going to have a recipe named after you!")

            messages.success(request, 'Thanking you for sending your ingredients we will get back you soon')
            return render(request, 'customer/sendingredients.html')
        except Exception  as e:

            print(str(e))
    messages.success(request, 'There is a problam in your ingredients')
    return render(request, 'customer/sendingredients.html')

def downloaditems(request):
    fooditems = addrecipemodel.objects.all()
    return render(request, 'customer/viewuploadfooditems.html', {'object': fooditems})

def recommend(request):
        if request.method == 'POST':
            form = recommendform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'you are successfully send message')
                return HttpResponseRedirect('customer/recommend.html')
            else:
                print('Invalid')
        else:
            form = recommendform()
        return render(request, "customer/recommend.html", {'form': form})

def recommended(request):
    email = request.session['email']
    recommenditems = recommendmodel.objects.filter(email=email)
    print("Recodem ",recommenditems)
    return render(request, "customer/recommended.html", {'form': recommenditems})

def foodcolor(request):
    return render(request,'customer/foodcolor.html',{})

def getfoodcolor(request):
    if request.method == 'POST':
        file = request.FILES.get('imgfile')
        #imgname = request.POST.get('imgname')
        #print("File Path ", type(file), " File name ", imgname)
        img = Image.open(file)
        img.save(settings.MEDIA_ROOT+"/cropped_picture.jpg")
        source_image = cv2.imread(settings.MEDIA_ROOT+"/cropped_picture.jpg")
        prediction = 'n.a.'
        PATH = './training.data'
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print('training data is ready, classifier is loading...')
        else:
            print('training data is being created...')
            open('training.data', 'w')
            color_histogram_feature_extraction.training()
            print('training data is ready, classifier is loading...')
        # get the prediction
        color_histogram_feature_extraction.color_histogram_of_test_image(source_image)
        prediction = knn_classifier.main('training.data', 'test.data')
        print('Pedection Color is ',prediction)
        cv2.putText(source_image,'Prediction: ' + prediction,(15, 45),cv2.FONT_HERSHEY_PLAIN,3,200,)
        # Display the resulting frame
        #cv2.imshow('color classifier', source_image)
        #cv2.waitKey(0)
        # imagedata = imagemodel.objects.all()
    return render(request, 'customer/fooddetect.html', {'color':prediction})



def recipes(request):
    email = request.session['email']
    sts = 'sent'
    dict = customeringredientsmodel.objects.filter(email=email,status=sts)
    return render(request,'customer/recipes.html',{'object':dict})

"""def detect(request):
    if request.method == "POST":
        imagename = request.GET.get('imagename')

        try:
            check = imagemodel.objects.get(imagename=imagename)
            file = check.file
            print(file)
            source_image = cv2.imread(file)
            prediction = 'n.a.'

            # checking whether the training data is ready
            PATH = './training.data'

            if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                print('training data is ready, classifier is loading...')
            else:
                print('training data is being created...')
                open('training.data', 'w')
                color_histogram_feature_extraction.training()
                print('training data is ready, classifier is loading...')

            # get the prediction
            color_histogram_feature_extraction.color_histogram_of_test_image(source_image)
            prediction = knn_classifier.main('training.data', 'test.data')
            cv2.putText(
                source_image,
                'Prediction: ' + prediction,
                (15, 45),
                cv2.FONT_HERSHEY_PLAIN,
                3,
                200,
            )

            # Display the resulting frame
            cv2.imshow('color classifier', source_image)
            cv2.waitKey(0)

            #imagedata = imagemodel.objects.all()
            return render(request, 'customer/fooddetect.html', )
        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request, 'Invalid Details')
        return render(request, 'customer/foodcolor.html')"""
