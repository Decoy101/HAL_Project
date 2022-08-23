from cProfile import label
from django import forms 
from django.forms import Form

from portal.models import SessionYearModel

class AddStudentForm(forms.Form):
    email = forms.EmailField(max_length=50,label='Email',widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=50,label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=50,label="First Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=50,label="Last Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(max_length = 50,label="Address",widget = forms.TextInput(attrs={"class":"form-control"}) )
    gender_list = (('M',"Male"),('F',"Female"))
    gender = forms.ChoiceField(label="Gender",choices= gender_list,widget = forms.Select(attrs={"class":"form-control"}))
    
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id,str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)

    except:
        session_year_list = []
    session_year_id = forms.ChoiceField(label = "Session Year", choices = session_year_list, widget = forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",required=False,widget=forms.FileInput(attrs={"class":"form-control"}))
    
    
    


