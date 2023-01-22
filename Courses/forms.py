from django import forms

class CreateNewDay(forms.Form):
  day_name = forms.CharField(label="Day's Name", max_length=20);


class CreateNewSuperUser(forms.Form):
  username = forms.CharField(label="User name", max_length=100);
  email = forms.CharField(label="Email", max_length=100);
  password = forms.CharField(label="Password", max_length=100);