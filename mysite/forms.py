from django import forms

from mysite.models import Person


class GetForm(forms.Form):
    first_cathetus = forms.IntegerField(label='first value', required=True, min_value=1)
    second_cathetus = forms.IntegerField(label='second value', required=True, min_value=1)


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
