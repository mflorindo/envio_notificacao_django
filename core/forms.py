from django.db.models.fields import CharField
from core.models import Application, Email, SMS, Templates, WebPush
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from django.forms import fields, models, widgets

from django.conf import settings


class FormLogin(AuthenticationForm):
    username = forms.CharField(
        max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class FormApplication(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user',)

    name = forms.CharField(max_length=50, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_web_push = forms.BooleanField(required=False)
    is_sms = forms.BooleanField(required=False)
    is_email = forms.BooleanField(required=False)


class FormWebPush(forms.ModelForm):
    class Meta:
        model = WebPush
        exclude = ('application',)

    site_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    site_url = forms.URLField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    icon = forms.FileField(max_length=200, required=False,
                           widget=forms.FileInput(attrs={'class': 'form-control'}))
    message_permission = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text_button_permission = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text_button_denied = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    title_welcome = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message_welcome = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_enabled_link = forms.BooleanField(
        required=False)
    link_destination = forms.URLField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class FormEmail(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ('application',)

    smtp_name = forms.CharField(label='Servidor SMTP', max_length=50,
                                required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    smtp_port = forms.IntegerField(label='Servidor Porta', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    login = forms.CharField(label='Usuário', max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', max_length=20, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender_name = forms.CharField(label='Nome de quem envia', max_length=50,
                                  required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender_email = forms.EmailField(label='Email de quem envia', max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email'}))

class FormSendEmail(forms.Form):
    emails_list = forms.CharField(label='Lista de Emails', max_length=1000, required=True,widget=forms.Textarea(attrs={'class':'form-control'}))
    template = models.ModelChoiceField(
        Templates.objects.all().order_by('title'),widget=forms.Select(attrs={'class': 'form-control','required':'required'}))
    application = models.ModelChoiceField(Application.objects.filter(is_email=True).order_by('name'),widget=forms.Select(attrs={'class': 'form-control','required':'required'}))


class FormTemplate(forms.ModelForm):
    class Meta:
        model = Templates
        fields = '__all__'

    title = forms.CharField(label='Título', max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    file = forms.FileField(label='Template', max_length=50, required=False,
                           widget=forms.FileInput(attrs={'accept': '*.html'})),

    def clean_file(self):
        file = self.cleaned_data['file']

        if file:
            file_type = file.content_type.split('/')[1]
            if len(file.name.split('.')) == 1:
                raise forms.ValidationError('Somente arquivos válidos')

            if file_type not in settings.TASK_UPLOAD_FILE_TYPES:
                raise forms.ValidationError('Somente arquivos html')

        return file


class FormSMS(forms.ModelForm):
    class Meta:
        model = SMS
        exclude = ('application',)

    provider = forms.CharField(label='Servidor', max_length=50, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    login = forms.CharField(label='Usuário', max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', max_length=20, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
