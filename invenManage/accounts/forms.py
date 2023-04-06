from django import forms


class SignupForm(forms.Form):
    class Meta:
        fields = ['username', 'email']
    name = forms.CharField(max_length=100)
    email = forms.EmailField()