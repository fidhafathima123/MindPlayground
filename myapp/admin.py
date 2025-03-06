from django.contrib import admin
from django.contrib.auth.models import User, Group
from trainerapp.models import Trainer
# Register your models here.
class TrainerProfileInline(admin.StackedInline):
    model = Trainer
    extra = 0  # No extra blank fields

# Custom User Admin with Trainer Profile Inline
class UserAdmin(admin.ModelAdmin):
    inlines = [TrainerProfileInline]
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')

# Unregister default User model and register our custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register Trainer Profile separately
admin.site.register(Trainer)



from django.contrib import admin
from django.contrib.auth.models import User
from healthproapp.models import HealthPro

# Inline model for HealthPro
class HealthProInline(admin.StackedInline):
    model = HealthPro
    extra = 0  # No extra blank fields

# Custom User Admin with HealthPro Inline
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [HealthProInline]
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')

# Unregister default User model and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register HealthPro separately
admin.site.register(HealthPro)




from django.contrib import admin
from django.contrib.auth.models import User
from guardianapp.models import Guardian

# Inline model for HealthPro
class GuardianInline(admin.StackedInline):
    model = Guardian
    extra = 0  # No extra blank fields

# Custom User Admin with HealthPro Inline
class GuardianUserAdmin(admin.ModelAdmin):
    inlines = [GuardianInline]
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')

# Unregister default User model and register our custom one
admin.site.unregister(User)
admin.site.register(User, GuardianUserAdmin)

# Register HealthPro separately
admin.site.register(Guardian)