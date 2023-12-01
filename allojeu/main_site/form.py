from django import forms
from .models import Post

class PostForm(forms.Form):
    avis = forms.CharField(widget=forms.Textarea)
    note = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 11)])
    #active = forms.ChoiceField(required=False, widget=forms.CheckboxInput)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['avis', 'note']

class RechercheForm(forms.Form):
    recherche = forms.CharField(label='Rechercher', max_length=100, required=False)
    date = forms.DateField(label='Jeux sortis après le',widget=forms.DateInput(attrs={'type': 'date'}), required=False)

