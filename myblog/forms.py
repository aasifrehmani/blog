from django import forms
from myblog.models import BlogPosts, Comments

class BlogPostForm(forms.ModelForm):
	class Meta:
		model	=	BlogPosts
		fields	=	('title', 'short_des', 'description')
		widgets	=	{
						'title' 		:	forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Title'}),
						'short_des'		:	forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Short Description'}),
						'description'	:	forms.Textarea(attrs = {'class':'form-control', 'placeholder':'Content', 'rows':'6'})
					}

class CommentForm(forms.ModelForm):
	class Meta:
		model 	=	Comments
		fields	=	('name', 'email', 'comment')
		widgets	=	{
						'name'		:	forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Enter your name'}),
						'email'		:	forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Enter your email'}),
						'comment'	:	forms.Textarea(attrs = {'class':'form-control', 'rows':'6', 'placeholder':'Enter your comment'})
					}