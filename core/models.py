from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, files
from django.utils.translation import gettext as _


class Application(models.Model):
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    is_web_push = models.BooleanField(_("Web Push"), default=False)
    is_sms = models.BooleanField(_("SMS"), default=False)
    is_email = models.BooleanField(_("Email"), default=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

class Templates(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    file = models.FileField(
        'Template', upload_to='template_email', max_length=100)

    def __str__(self):
        return self.title

class Email(models.Model):
    application = models.OneToOneField(
        Application, related_name='email', on_delete=models.CASCADE)
    smtp_name = models.CharField(_("SMTP Name"), max_length=50)
    smtp_port = models.SmallIntegerField(_("SMTP Port"))
    login = models.CharField(_("Login"), max_length=50)
    password = models.CharField(_("Password"), max_length=50)
    sender_name = models.CharField(_("Sender Name"), max_length=50)
    sender_email = models.CharField(_("Sender Email"), max_length=50)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.smtp_name + ' - ' + self.application.name





class SMS(models.Model):
    application = models.OneToOneField(
        Application, related_name='sms', on_delete=models.CASCADE)
    provider = models.CharField(_("Provider"), max_length=50)
    login = models.CharField(_("login"), max_length=50)
    password = models.CharField(_("Password"), max_length=50)

    objects = models.Manager()

    class Meta:
        verbose_name = _("SMS")
        verbose_name_plural = _("SMS")

    def __str__(self):
        return self.provider + ' - ' + self.application.name


class WebPush(models.Model):
    application = models.OneToOneField(
        Application, related_name='webpush', on_delete=models.CASCADE)
    site_name = models.CharField(_("Site Name"), max_length=50)
    site_url = models.CharField(_("Site URL"), max_length=50)
    icon = models.FileField(_("Icon"), upload_to='icons', max_length=100)
    message_permission = models.CharField(
        _("Message Permission"), max_length=100)
    text_button_permission = models.CharField(
        _("Text Button Permission"), max_length=50)
    text_button_denied = models.CharField(
        _("Text Button Denied"), max_length=50)
    title_welcome = models.CharField(_("Title Welcome"), max_length=50)
    message_welcome = models.CharField(_("Message Welcome"), max_length=100)
    is_enabled_link = models.BooleanField(_("Enabled Link"), default=False)
    link_destination = models.CharField(_("Link Destination"), max_length=50)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.site_name + ' - '+self.application.name


class Notification(models.Model):

    SOURCE = (
        ('API', 'API'),
        ('PLA', 'Plataforma'),
    )


    

    sms = models.ForeignKey(SMS, on_delete=models.CASCADE, blank=True,null=True)
    webpush = models.ForeignKey(WebPush, on_delete=models.CASCADE, blank=True,null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, blank=True,null=True)
    send_date = models.DateField(auto_now=False, auto_now_add=False)
    reading_date = models.DateField(auto_now=False, auto_now_add=False)
    confirmation = models.BooleanField(default=False)
    source = models.CharField(max_length=3, choices=SOURCE)
    content = models.TextField(null=True)

    def __str__(self):
        if self.sms is not None:
            return 'Envio por SMS : ' + self.sms.provider
        if self.email is not None:
            return 'Envio por Email : ' + self.email.smtp_name
        if self.webpush is not None:
            return 'Envio por Web Push : ' + self.webpush.site_name
    
