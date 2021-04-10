from django import forms

from .models import Post,Comment


class PostCreateForm(forms.ModelForm):
    interest=forms.CharField(required=False,max_length=200,widget=forms.TextInput(attrs={'placeholder': 'For Exchange Post'}))
    period=forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder': 'For Rent Post'}))
    price=forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder': 'For Sale Post'}))
    condition=forms.CharField(required=False,max_length=200,widget=forms.TextInput(attrs={'placeholder': 'For Sale Post'}))
    class Meta:
        model=Post
        fields=[
            'title',
            'type',
            'description',
            'address',
            'post_image',
            'price',
            'condition',
            'period',
            'interest',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
