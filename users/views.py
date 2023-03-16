# users/views.py

# render function imported from Django's 'shortcuts' module. render func helps
# render a template with a context and return an HTTP response
# Connect to urls.py to map a URL path to dashboard

from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm

# Define the 'dashboard' view function
# request object is an instance of the HttpRequest class.
def dashboard(request):
    # Render the dashboard template and returns the resulting HTTP response
    return render(request, "users/dashboard.html")

def register(request):
    # If the request method is 'GET', display the registration form
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}  # Pass the custom user creation form to the template
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Making changes to ensure normal user creation works with GitHub
            # creaton
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request,user)
            return redirect(reverse("dashboard"))

