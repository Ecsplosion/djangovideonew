from django import forms
from . models import Video, UserProfile
from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class VideoSubmitForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter a title...", "id":"video-title-field"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter video description...", "id" : "video-desc-field"}))
    video = forms.FileField(widget=forms.FileInput(attrs={"id":"video-input-field"}))
    class Meta:
        model=Video
        fields = ["title", "description", "video"]
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name...", "id":"first_name","class":"signup-form-fields", "type":"text"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name...", "id":"last_name","class":"signup-form-fields", "type":"text"}))
    username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter an email address...', 'class': "signup-form-fields", "type":"email", "onfocus": "this.removeAttribute('readonly');", "id": "email", "autocomplete": "off"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter a strong password...', 'class': "signup-form-fields", "type":"password", "onfocus": "this.removeAttribute('readonly');", "id": "password1", "autocomplete": "off"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password...', 'class': "signup-form-fields", "type":"password", "onfocus": "this.removeAttribute('readonly');", "id": "password2", "autocomplete": "off"}))
    
    class Meta:
        model = User
        fields =["username", "first_name", "last_name", "password1", "password2"]
class UserProfileForm(forms.ModelForm):
    channel_logo = forms.ImageField(label= "Choose an Image", widget=forms.ClearableFileInput(attrs={"class": "image_upload_field", "value":"Upload Image"}))

    class Meta:
        model = UserProfile
        fields = ["channel_logo"]
        # help_texts = {
        #     'channel_logo': None
        # }
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #     self.fields["channel_logo"].help_text = None
    