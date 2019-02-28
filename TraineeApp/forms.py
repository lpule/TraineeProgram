from django import forms

from .models import Post, Author, Editor


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish_date', 'author', 'editor', 'draft']


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    publish_date = forms.DateField()
    author = forms.MultipleChoiceField()
    editor = forms.MultipleChoiceField()
    draft = forms.BooleanField()
