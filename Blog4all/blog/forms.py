from django import forms
from blog.models import Blogpost,Comment

class BlogpostForm(forms.ModelForm):
    
    class Meta():
        model = Blogpost
        fields = ('author','topic','title','text')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'textinput'}), # we will have to define textinput class in css file
            'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author' : forms.TextInput(attrs={'class' : 'textinput'}),
            'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea'})
        }

