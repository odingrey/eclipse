from django import forms
from eclipse.models.eclipseuser import EclipseUser


class UserProfile(forms.ModelForm):
	class Meta:
		model = EclipseUser
		fields = ('full_name',)
