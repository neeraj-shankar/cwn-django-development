from django import forms
from django.forms import ModelForm


from BlogApp.models import Category,Post

choices = Category.objects.all().values_list('title', 'title')

choices_list = []

for item in choices:
    choices_list.append(item)

#***************************** creating form for Post Category**************************

class CategoryForm(ModelForm):

    class Meta:
        model = Category

        #list of fields - to add post category
        fields = ('img','title', 'desc', 'slug')

        #labels for the each field
        labels = { 'img': '','title': '','desc': '','slug': ''

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Category Title '}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder' :'Description'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'SlugField'}),
    
        }

class PostForm(ModelForm):
    class Meta:
        model = Post

        # list of fields 
        fields = ('title', 'category', 'author', 'img', 
        'desc', 'slug')

        # labels 
        labels = {'title':'', 'category':'', 
        'author':'', 'img':'', 'desc':'', 'slug':''}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(choices=choices_list ,attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'author': forms.Select(attrs={'class': 'form-control','placeholder': 'Author',}),
            'date': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Date',}),

            'desc' : forms.Textarea(attrs={'class': 'form-control','placeholder': 'Description',}),
            'slug': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Slug Area',})
        }



