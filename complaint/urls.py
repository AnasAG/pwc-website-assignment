from django.urls import path

from . import views

urlpatterns = [
    # todo:
    path('', views.login),
    path('registration/', views.registration),
    path('complaint/', views.add_complaint),
]