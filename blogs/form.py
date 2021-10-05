from django import forms

from .models import BlogDetail


class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = BlogDetail
        fields = '__all__'
        exclude = ('id',)
