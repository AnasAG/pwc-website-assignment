from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms


def add_complaint(request):
    # check if the http request is POST method 
    if request.method == 'POST':
        form = models.Complaint(request.POST or None)
        # check if data in form is considered valid
        if form.is_valid():
            # save/update changes
            form.save()
        # full_name = request.POST.get('full_name')
        # email = request.POST.get('email')
        # complaint = request.POST.get('complaint')
        # complaint_type = request.POST.get('complaint_type')
    else:
            form = models.Complaint()
    context = {'form': form}
    return render(request, 'complaint_webpage.html', context)

def view_complaints(request):
    # view all complaint objects
    form = models.Complaint.objects.all()
    context = {'form': form}
    # todo: raplace with 'customer_homepage.html'
    return render(request, 'customer_homepage.html', context)

def login(request):
    context = {}
    return render(request, 'login_webpage.html', context)

def registration(request):
    context = {}
    return render(request, 'registration_webpage.html', context)