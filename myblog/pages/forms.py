from django import forms
from .models import Post, Category

category_all = Category.objects.all().values_list('name', 'name')
categories = [item for item in category_all]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'snippet', 'body')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please insert a title..."}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(choices=categories, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type your post here..."}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your snippet here..."}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please insert a title..."}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(choices=categories, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type your post here..."}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your snippet here..."}),

        }
