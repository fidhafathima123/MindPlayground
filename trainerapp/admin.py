# admin.py (trainerapp/admin.py)
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Trainer
from .forms import TrainerCreationForm

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'specialization', 'experience', 'is_active')
    form = TrainerCreationForm
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only for new trainers
            # The user is already created in the form's save method
            pass
        obj.save()

# Remove the @admin.register decorator and any previous registrations
try:
    admin.site.unregister(Trainer)
except admin.sites.NotRegistered:
    pass

# Register once
admin.site.register(Trainer, TrainerAdmin)