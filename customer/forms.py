from django import forms

from customer.models import customerregistrationmodel, customeringredientsmodel, recommendmodel


class customerregistrationform(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(),required=True)
    mobile = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    address = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    state = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = customerregistrationmodel
        fields = ['first_name','last_name','loginid','password','email','mobile','address','state','authkey','status' ]



class customeringredientsform(forms.ModelForm):
    class Meta:
        model = customeringredientsmodel
        fields = ['loginid','email','ingredients','recipes','descriptions','status','name']


class recommendform(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(), required=True)
    recommend = forms.CharField(widget=forms.TextInput(), required=True, max_length=500)

    class Meta:
        model = recommendmodel
        fields = ['email', 'recommend']


"""class imagemodelForm(forms.ModelForm):

    class Meta:
        model = imagemodel
        fields = ('imagename','file')"""

