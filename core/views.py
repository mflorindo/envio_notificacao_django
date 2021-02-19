from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models

from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

from django.views.generic import CreateView, ListView, TemplateView,FormView
from django.views.generic.edit import DeleteView, UpdateView

from core.forms import FormApplication, FormEmail, FormLogin, FormSMS, FormSendEmail, FormTemplate, FormWebPush
from core.models import Application, Email, Notification, SMS, Templates, WebPush
from django.db.models import ProtectedError
from django.contrib import messages
from datetime import date, datetime, timedelta
import random as r


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class ApplicationListView(LoginRequiredMixin, ListView):
    template_name = 'application_list.html'
    queryset = Application.objects.all()
    context_object_name = 'objects'


class ApplicationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Application
    form_class = FormApplication
    template_name = 'application.html'
    success_url = '/applications/'
    success_message = "Aplicação inserida com sucesso"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ApplicationUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Application
    form_class = FormApplication
    template_name = 'application.html'
    success_url = '/applications/'
    success_message = "Aplicação alterada com sucesso"


class ApplicationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Application
    success_message = 'Aplicação excluída com sucesso'
    success_url = '/applications/'
    template_name = 'application_confirm_delete.html'


''' WEBPUSH '''


class WebPushCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = WebPush
    form_class = FormWebPush
    template_name = 'webpush.html'
    success_url = '/applications/'
    success_message = 'Web Push inserido com sucesso'

    def form_valid(self, form):
        form.instance.application = Application.objects.get(
            pk=self.kwargs.get('application'))
        return super().form_valid(form)


class WebPushUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = WebPush
    form_class = FormWebPush
    template_name = 'webpush.html'
    success_url = '/applications/'
    success_message = 'Web Push alterado com sucesso'


class WebPushDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = WebPush
    success_message = 'Web Push excluído com sucesso'
    success_url = '/applications/'
    template_name = 'webpush_confirm_delete.html'


''' EMAIL '''


class EmailCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Email
    form_class = FormEmail
    template_name = 'email.html'
    success_url = '/applications/'
    success_message = 'Email inserido com sucesso'

    def form_valid(self, form):
        form.instance.application = Application.objects.get(
            pk=self.kwargs.get('application'))
        return super().form_valid(form)


class EmailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Email
    form_class = FormEmail
    template_name = 'email.html'
    success_url = '/applications/'
    success_message = 'Email alterado com sucesso'


class EmailDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Email
    success_message = 'Email excluído com sucesso'
    success_url = '/applications/'
    template_name = 'email_confirm_delete.html'


''' SMS '''


class SMSCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SMS
    form_class = FormSMS
    template_name = 'sms.html'
    success_url = '/applications/'
    success_message = 'SMS inserido com sucesso'

    def form_valid(self, form):
        form.instance.application = Application.objects.get(
            pk=self.kwargs.get('application'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['application'] = Application.objects.get(
            pk=self.kwargs.get('application'))
        return ctx


class SMSUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SMS
    form_class = FormSMS
    template_name = 'sms.html'
    success_url = '/applications/'
    success_message = 'SMS alterado com sucesso'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['application'] = self.object.application
        return ctx


class SMSDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SMS
    success_message = 'SMS excluído com sucesso'
    success_url = '/applications/'
    template_name = 'sms_confirm_delete.html'


''' TEMPLATE '''


class TemplatesListView(LoginRequiredMixin, ListView):
    template_name = 'template_list.html'
    queryset = Templates.objects.all()
    context_object_name = 'objects'


class TemplatesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Templates
    form_class = FormTemplate
    template_name = 'template.html'
    success_url = '/template/'
    success_message = 'Template inserido com sucesso'


class TemplatesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Templates
    success_message = 'Template excluído com sucesso'
    success_url = '/template/'
    template_name = 'template_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.add_message(
                request, messages.ERROR, 'Este template está vinculado a um ou mais emails. Não poderá ser excluído!')
            return redirect('/template')




class AccessView(LoginView):
    template_name = 'login.html'
    authentication_form = FormLogin


def logout_view(request):
    logout(request)
    return redirect('login')
