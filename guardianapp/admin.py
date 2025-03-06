from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Guardian
from .forms import GuardianRegistrationForm

class GuardianAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address','occupation','place')
    form = GuardianRegistrationForm
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only for new trainers
            # The user is already created in the form's save method
            pass
        obj.save()

# Remove the @admin.register decorator and any previous registrations
try:
    admin.site.unregister(Guardian)
except admin.sites.NotRegistered:
    pass

# Register once
admin.site.register(Guardian, GuardianAdmin)
