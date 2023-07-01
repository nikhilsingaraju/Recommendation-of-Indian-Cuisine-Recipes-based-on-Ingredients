from django.db import models

# Create your models here.
class foodcourtregistrationmodel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email



class addrecipemodel(models.Model):
    recipename = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.recipename


"""class foodcourtsendrecipesmodel(models.Model):
    loginid = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    recipe1 = models.CharField(max_length=100)
    recipe2 = models.CharField(max_length=100)
    recipe3 = models.CharField(max_length=100)
    recipe4 = models.CharField(max_length=100)
    recipe5 = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email"""