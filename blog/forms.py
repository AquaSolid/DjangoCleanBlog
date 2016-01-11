from django import forms
from .models import Blog
import datetime

class PostForm(forms.Form):
	title = forms.CharField()
	subtitle = forms.CharField(required=False)
	date_added = forms.DateTimeField()
	image = forms.URLField(required=False)
	tags = forms.CharField(required=False)
	article = forms.CharField()
	author = forms.CharField()

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle',
        			'image', 'tags',  'article')
    