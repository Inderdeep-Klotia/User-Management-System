# users/urls.py

# Import the `path` function from Django's `urls` module.
# Function used to create URL patterns.
# include function used to include a set of URL patterns from another module.
from django.urls import path, include
# Import `dashboard` view function from `users.views` module.
from users.views import dashboard, register

# Django uses this list to match incoming URLs to their corresponding
# view functions.
urlpatterns = [
    # Create URL pattern for`dashboard` view
    # When user visits "/dashboard/" URL path, the `dashboard`
    # call view function
    # The `name` parameter used to give URL pattern a unique identifier.
    path("dashboard/", dashboard, name="dashboard"),

    # include Django authentation URL patterns under /accounts/
    # ENABLES FOLLOWING VIEWS:
    # /accounts/login/ - Login view
    # /accounts/logout/ - Logout view
    # /accounts/password_change/ - Password change view
    # /accounts/password_change/done/ - Password change success view
    # /accounts/password_reset/ - Password reset view
    # /accounts/password_reset/done/ - Password reset request success view
    # /accounts/reset/<uidb64>/<token>/ - Password reset confirmation view
    # /accounts/reset/done/ - Password reset complete view
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),




]