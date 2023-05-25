"""digital_society URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from societymemberapp import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('society-profile/', views.society_profile, name='society-profile'),
    path('society-change-password/', views.society_change_password, name='society-change-password'),
    path('society-view-notice/', views.society_view_notice, name='society-view-notice'),
    path('society-view-details/<int:pk>', views.society_view_details, name='society-view-details'),
    path('society-view-event/', views.society_view_event, name='society-view-event'),
    path('society-view-event-details/<int:pk>', views.society_view_event_details, name='society-view-event-details'),
    path('add-complaint/', views.add_complaint, name='add-complaint'),
    path('society-view-complaint/', views.society_view_complaint, name='society-view-complaint'),
    path('society-complaint-details/<int:pk>', views.society_complaint_details, name='society-complaint-details'),
     path('society-contact-list/', views.contact_list, name='society-contact-list'),
    
]
