from django.db import models

# Create your models here.
class customerregistrationmodel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class customeringredientsmodel(models.Model):
    id = models.AutoField(primary_key=True)
    loginid = models.CharField(max_length=100)
    email = models.EmailField()
    ingredients = models.CharField(max_length=600)
    recipes = models.CharField(max_length=250)
    descriptions = models.CharField(max_length=600)
    status = models.CharField(max_length=600, default='waiting')
    name = models.CharField(max_length=600, default='notassigned')

    def __str__(self):
        return self.email


class recommendmodel(models.Model):
    email = models.CharField(max_length=100)
    recommend = models.CharField(max_length=500)

    def __str__(self):
        return self.email


"""class imagemodel(models.Model):
    imagename = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.imagename"""