from django import forms
from django.forms import ModelForm
from .models import User, Material, Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['about','content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(PostForm, self).__init__(*args, **kwargs)
        # self.fields['about']=forms.ModelChoiceField(queryset=Material.objects.filter(owner=self.user).order_by('-startDate'))
        self.fields['content']=forms.CharField(max_length=500)
        self.fields['about'].queryset=Material.objects.filter(owner=self.user).order_by('-startDate')