from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from .models import HealthPro
from .forms import HealthproCreationForm

class HealthProAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'phone','specialization','date_joined','certification')
    form = HealthproCreationForm
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only for new trainers
            # The user is already created in the form's save method
            pass
        obj.save()

# Remove the @admin.register decorator and any previous registrations
try:
    admin.site.unregister(HealthPro)
except admin.sites.NotRegistered:
    pass

# Register once
admin.site.register(HealthPro, HealthProAdmin)