from dataclasses import field
from django import forms
from pages.models import Blog, Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= "__all__"
        


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields= "__all__"


        