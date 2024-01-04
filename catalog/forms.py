from django import forms
from datetime import date 
from catalog.models import Author


class Form_add_author(forms.Form):
    first_name = forms.CharField(label="Name author")
    last_name = forms.CharField(label="Last author")
    date_of_birth = forms.DateField(label="Date of birth", initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={"type": 'date'}))
    about = forms.CharField(label="About author")
    photo = forms.ImageField(label="Image author")



class Form_edit_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
