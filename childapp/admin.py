from django.contrib import admin
from .models import Child
from .forms import ChildRegistrationForm, ChildUpdateForm

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    # Use the custom form for adding/editing Child instances
    form = ChildUpdateForm
    add_form = ChildRegistrationForm

    # Fields to display in the list view
    list_display = (
          # Use the method to display full name
        'date_of_birth',
        'age',            # Use the method to display age
        'gender',
        'guardian',
        'assigned_trainer',
        'assigned_health_professional',
        'is_active',
    )

    # Fields to filter the list view
    list_filter = (
        'gender',
        'is_active',
        'guardian',
        'assigned_trainer',
        'assigned_health_professional',
    )

    # Fields to search in the list view
    search_fields = (
        
        
        'guardian__username',  # Search by guardian's username
        'assigned_trainer__username',  # Search by trainer's username
        'assigned_health_professional__username',  # Search by health professional's username
    )

    # Fields to display in the detail/edit view
    fieldsets = (
        ('Core Information', {
            'fields': (
                
                'date_of_birth',
                'gender',
                'place',
                'phone',
                'hobbies',
                'interests',
                
            ),
        }),
        ('Relationships', {
            'fields': (
                'guardian',
                'assigned_trainer',
                'assigned_health_professional',
            ),
        }),
        ('Additional Information', {
            'fields': (
                'emergency_contact',
                
                'medical_conditions',
                'allergies',
                'school_name',
                'grade_level',
                'profile_photo',
            ),
        }),
        ('Status', {
            'fields': (
                'is_active',
            ),
        }),
    )

    # Read-only fields in the detail/edit view
    readonly_fields = (
        'registration_date',
        'last_updated',
        'age',  # Age is calculated, so it should be read-only
    )

    # Custom method to display full name in the list view
     # Column header in the list view

    # Custom method to display age in the list view
    def age(self, obj):
        return obj.age()
    age.short_description = 'Age'  # Column header in the list view

    # Use the add_form for the add view
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            # Use the add form for creating a new Child
            return self.add_form
        return super().get_form(request, obj, **kwargs)