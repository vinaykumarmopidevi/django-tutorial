from django import forms
from django.core.validators import EmailValidator,MinLengthValidator
from django.core.exceptions import ValidationError


def check_for_m(value):
    if value[0].lower() != 'm':
        raise forms.ValidationError('Name should be start with m')


class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_m,MinLengthValidator(8)])
    email=forms.EmailField(validators=[EmailValidator(message="Invalid email address")])
    verify_email=forms.EmailField(validators=[EmailValidator(message="Invalid email address")])
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data=super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email !=vmail:
            raise ValidationError(f"The emails {email} and {vmail} are not matching")

    


