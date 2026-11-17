from django.forms import ModelForm
from sports.models import Tournament,Sport,Team,Fixture,Result,Stat
from django import forms

class TournamentForm(ModelForm):
    
    class Meta:
        model=Tournament
        fields='__all__'
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control flatpickr'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control flatpickr'}),
        }


        


class SportForm(ModelForm):
    
     class Meta:
         model=Sport
         fields='__all__'



class TeamForm(ModelForm):
    
     class Meta:
         model=Team
         fields='__all__'



class FixtureForm(ModelForm):
    
     class Meta:
         model=Fixture
         fields='__all__'
         widgets = {
            'fixture_date': forms.TextInput(attrs={'class': 'form-control flatpickr'}),
        }




class ResultForm(ModelForm):
    
     class Meta:
         model=Result
         fields='__all__'



class StatForm(ModelForm):
    
     class Meta:
         model=Stat
         fields='__all__'


