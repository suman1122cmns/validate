from django import forms
def check_for_A(value):
    if value.lower().startswith('a'):
        raise forms.ValidationError('nAME IS started with a')

def check_for_len(value):
    if len(value)>=10:
        raise forms.ValidationError('length issue')


class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_A,check_for_len])
    age=forms.IntegerField(min_value=18,max_value=60)
    mobile=forms.CharField(min_length=10,max_length=10)