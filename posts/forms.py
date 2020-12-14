from django import forms

from .models import Post, Images, Contact

class PostForms(forms.ModelForm):
	publish = forms.DateField(label = '', widget=forms.SelectDateWidget)
	title = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))
	
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish",

		]
class ImageForms(forms.ModelForm):
	image = forms.ImageField(label='Image')

	class Meta:
		model = Images
		fields = ('image',)

class CantactForms(forms.ModelForm):
	full_name = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	phone = forms.CharField(widget=forms.NumberInput(attrs={
		'class': 'form-control'
	}))

	email = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	subject = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	message = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))

	class Meta:
		model = Contact
		fields = [
			"full_name",
			"phone",
			"email",
			"subject",
			"message",
		]

