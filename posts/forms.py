from django import forms

class ContactForm(forms.Form):
     # from_email = forms.EmailField(required=True)
     subject = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
     message = forms.CharField(widget=forms.Textarea, required=True,help_text='Please write your name and contact information')