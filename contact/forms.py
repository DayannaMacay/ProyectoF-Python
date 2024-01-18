from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control bg-transparent', 'placeholder':'Nombre'}
    ))
    email=forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control bg-transparent', 'placeholder':'Email'}
    ))
    affair=forms.CharField(label='Asunto', required=True, widget=forms.TextInput(
        attrs={'class':'form-control bg-transparent', 'placeholder':'Asunto'}
    ))
    message=forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'class':'form-control bg-transparent', 'rows':4, 'placeholder':'Mensaje'}
    ), min_length=10, max_length='500')