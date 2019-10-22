from django import forms
from .models import Post, Image


class TweetForm(forms.Form):
    tweet = forms.CharField(max_length=140, required=True)
    images = forms.ImageField(required=False,
                              widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
