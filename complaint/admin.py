from django.contrib import admin

from .models import UserEmail, Complaint

admin.site.register(UserEmail)
admin.site.register(Complaint)