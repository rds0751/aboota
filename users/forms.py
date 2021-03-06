from allauth.account.forms import SignupForm
from django import forms
from binary.models import BinaryTree
from .models import *
import random

class SimpleSignupForm(SignupForm):
	mobile = forms.CharField(max_length=250, label='mobile')
	name = forms.CharField(max_length=250, label='name')
	referal_code = forms.CharField(max_length=14, label="refer")

	def get_success_url(self):
		return '/signup/onboarding/'
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'mobile')

	def clean_name(self):
		name = self.cleaned_data['name']
		return name[0].upper() + name[1:].lower()

	# def clean_username(self):
	# 	def generateuser():
	# 		r = random.randint(100000,9999999)
	# 		u = User.objects.filter(username='JR{}'.format(r)).count()
	# 		if u > 0:
	# 			generateuser()
	# 		else:
	# 			return 'JR{}'.format(r)
	# 	u = generateuser()
	# 	username = u
	# 	return username

	def save(self, request):
		user = super(SimpleSignupForm, self).save(request)
		user.mobile = self.cleaned_data['mobile']
		user.name = self.cleaned_data['name']
		user.referal = self.cleaned_data['referal_code']
		user.save()
		return user