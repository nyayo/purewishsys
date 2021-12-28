from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Posts, Donor, Messages, Volunteer, Stuff, Gallery, ProjectManager, Profile


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'post']


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['username', 'first_name', 'second_name',
                  'email', 'organisation', 'country', 'phone', 'image']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message']


class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['stuff', 'first_name',
                  'second_name', 'email', 'phone', 'role']


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['volunteer', 'first_name', 'second_name', 'email', 'phone']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']


class MailForm(forms.Form):
    sender = forms.EmailField()
    receiver = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ['project', 'description',
                  'sponsors', 'project_manager', 'theme']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
