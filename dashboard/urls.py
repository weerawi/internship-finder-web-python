from django.urls import path
from . import views

urlpatterns= [
    path('',views.dashboard,name='proxy'),
    path('applicant-dashboard/',views.applicant_dashboard,name='applicant_dashboard'),
    path('recruiter-dashboard/',views.recruiter_dashboard,name='recruiter_dashboard'),
]