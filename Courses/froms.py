from django import forms

class CreateNewDay(forms.Form):
  day_name = forms.CharField(label="Day's Name", max_length=20);
