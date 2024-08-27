from django import forms

class UserInfoForm(forms.Form):
    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UK', 'United Kingdom'),
        # Add more countries as needed
    ]
    
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('FR', 'French'),
        ('SP', 'Spanish'),
        # Add more languages as needed
    ]

    name = forms.CharField(
        max_length=100, 
        label='Full Name', 
        widget=forms.TextInput(attrs={'class': '.custom-input'})
    )
    email = forms.EmailField(
        label='Email Address', 
        widget=forms.EmailInput(attrs={'class': '.custom-input'})
    )
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES, 
        label='Country', 
        widget=forms.Select(attrs={'class': '.custom-input'})
    )
    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES, 
        label='Preferred Language', 
        widget=forms.Select(attrs={'class': '.custom-input'})
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': '.custom-input'}), 
        label='Short Bio'
    )

    # Add more fields as needed
