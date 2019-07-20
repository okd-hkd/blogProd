from django import forms
# from .models import Post


# class PostSearchForm(forms.ModelForm):
#      category_name = forms.CharField(label='カテゴリ名', required=False)
#
#      class Meta:
#           model = Post
#           fields = (
#                'category.name',
#           )



class ContactForm(forms.Form):
     # from_email = forms.EmailField(required=True)
     subject = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
     message = forms.CharField(widget=forms.Textarea, required=True,help_text='Please write your name and contact information')