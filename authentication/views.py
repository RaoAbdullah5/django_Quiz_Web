from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Ensure this matches your actual form name
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':  # Check if form data was submitted
        form = RegistrationForm(request.POST)  # Bind form to POST data
        if form.is_valid():  # Validate the form
            form.save()  # Save the new user
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to login page
        else:
            print(form.errors)  # Debugging
    else:
        form = RegistrationForm()  # Instantiate an empty form
    return render(request, 'register.html', {'form': form})


# @login_required
# def home(request):
#     obj= User.objects.all()

#     return render(request, 'home.html', {'obj': obj})


    