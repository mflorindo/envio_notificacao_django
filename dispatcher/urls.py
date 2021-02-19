"""dispatcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import ApplicationCreateView, ApplicationDeleteView, ApplicationUpdateView, DashboardView, AccessView, ApplicationListView, EmailCreateView, EmailDeleteView, EmailUpdateView, SMSCreateView, SMSDeleteView, SMSUpdateView, TemplatesCreateView, TemplatesDeleteView, TemplatesListView, WebPushCreateView, WebPushDeleteView, WebPushUpdateView, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', AccessView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('applications/add/', ApplicationCreateView.as_view(),
         name='application_new'),
    path('application/edit/<int:pk>', ApplicationUpdateView.as_view(),
         name='application_update'),
    path('application/delete/<int:pk>', ApplicationDeleteView.as_view(),
         name='application_delete'),

    path('webpush/add/<int:application>',
         WebPushCreateView.as_view(), name='webpush_new'),
    path('webpush/edit/<int:pk>',
         WebPushUpdateView.as_view(), name='webpush_update'),
    path('webpush/delete/<int:pk>',
         WebPushDeleteView.as_view(), name='webpush_delete'),

    path('email/add/<int:application>',
         EmailCreateView.as_view(), name='email_new'),
    path('email/edit/<int:pk>',
         EmailUpdateView.as_view(), name='email_update'),
    path('email/delete/<int:pk>',
         EmailDeleteView.as_view(), name='email_delete'),

    path('sms/add/<int:application>',
         SMSCreateView.as_view(), name='sms_new'),
    path('sms/edit/<int:pk>',
         SMSUpdateView.as_view(), name='sms_update'),
    path('sms/delete/<int:pk>',
         SMSDeleteView.as_view(), name='sms_delete'),

    path('template/', TemplatesListView.as_view(), name='template_list'),
    path('template/add/',
         TemplatesCreateView.as_view(), name='template_new'),
    path('template/delete/<int:pk>',
         TemplatesDeleteView.as_view(), name='template_delete'),
      


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
