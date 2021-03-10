from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms


def add_complaint(request):
    if request.method == 'POST':
        # instance = models.Complaint.objects.get(id=1)
        form = models.Complaint(request.POST or None)   # , instance)
        print("\n\n This is the form object: \n\n", form)
        print("\n\n This the form type: \n\n", type(form))
        print("\n\n This is the form id: \n\n", form.id)
        # if form.is_valid():
        form.save()
        # full_name = request.POST.get('full_name')
        # email = request.POST.get('email')
        # complaint = request.POST.get('complaint')
        # complaint_type = request.POST.get('complaint_type')
        # print("Info recieved", full_name, email, complaint, complaint_type)
    else:
            form = models.Complaint()
    context = {'form': form}
    # context["dataset"] = models.Complaint.objects.all()
    return render(request, 'complaint_webpage.html', context)


# Delete _______________________________________________________________________
def login(request):
    context = {}
    context["dataset"] = models.UserEmail.objects.all()
    return render(request, 'login_webpage.html', context)

def registration(request):
    context ={}
    # add the dictionary during initialization
    context["dataset"] = models.UserEmail.objects.all()
    return render(request, "registration_webpage.html", context)


