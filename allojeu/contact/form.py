from django import forms
from .models import Contact



class ContactForm(forms.Form):
    avis = forms.CharField(widget=forms.Textarea)
    note = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 11)])
    #active = forms.ChoiceField(required=False, widget=forms.CheckboxInput)

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'name', 'email', 'content']
