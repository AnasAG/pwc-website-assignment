from django.db import models
from django.forms import ModelForm

class UserEmail(models.Model):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
    )
    user_email = models.EmailField()
    # todo: modify user_type with the suitable data type
    user_type = models.CharField(max_length=140, choices = USER_TYPE)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_email

class Complaint(models.Model):
    COMPLAINT_STATUS = (
        ('Reviewing', 'Reviewing'),
        ('Resovled', 'Resovled'),
        ('Canceled', 'Canceled'),
    )
    # complaint_for_user = models.ForeignKey('UserEmail', default = 1,  on_delete=models.CASCADE)
    # complaint_date = models.DateField(blank=True, null=True)
    complaint_content = models.TextField()
    complaint_status = models.CharField(max_length=140, choices=COMPLAINT_STATUS)

    def __str__(self):
        return self.complaint_content

