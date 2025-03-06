from django.shortcuts import render,redirect
from guardianapp.forms import GuardianRegistrationForm

from django.contrib import messages

# Create your views here.
def guardian_dashboard(request):
    return render(request,"guardian/guardian_dashboard.html")

def registration(request):
    print(" registration")
    if request.method == 'POST':
        form = GuardianRegistrationForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            messages.success(request, "Registration successful!")
            return redirect("guardian_dashboard")  # Adjust this to your actual success URL
        else:
            print("Invalid")
            # Print form errors for debugging
            print(form.errors)  # This will output errors to the console
            messages.error(request, "Please correct the errors below.")
    else:
        form = GuardianRegistrationForm()
    
    return render(request,'registration.html', {'form': form})