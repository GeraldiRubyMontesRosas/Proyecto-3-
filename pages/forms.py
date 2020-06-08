from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widget ={
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
            'content' :forms.Textarea(attrs={'class':'form-control',}),
            'order' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
        }
        labels ={
            'title':'','order':'','content':''
        }