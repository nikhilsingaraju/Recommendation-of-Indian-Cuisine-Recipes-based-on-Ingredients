from django import forms

from foodcourt.models import foodcourtregistrationmodel, addrecipemodel


class foodcourtregistrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(),required=True)
    mobile = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    address = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = foodcourtregistrationmodel
        fields = ['name','loginid','password','email','mobile','address','authkey','status' ]


class addrecipeForm(forms.ModelForm):

    class Meta:
        model = addrecipemodel
        fields = ('recipename','ingredients','description','file')