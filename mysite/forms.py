from django import forms


class GetForm(forms.Form):
    first_cathetus = forms.IntegerField(label='first value', required=True, min_value=1)
    second_cathetus = forms.IntegerField(label='second value', required=True, min_value=1)
