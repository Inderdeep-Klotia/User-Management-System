"""
users/forms.py
forms.py file should not be placed under templates as it contains Python code
related to forms and not template files. Template folder used for storing HTML
template files only.

Storing it directly under the users app follows correct Django convention, and
allows it to be easily imported and used within views.
"""

# Import the built-in UserCreationForm from Django. Default form for creating
# new user instances, including fields for username, password, password conf
from django.contrib.auth.forms import UserCreationForm


# Define a CustomUserCreationForm that inherits from the built-in
# UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Define the inner Meta class to customize the form's behavior. 'Meta'
    # used to modify behavior of the form (or a model).
    class Meta(UserCreationForm.Meta):
        # Specifies which fields should be displayed in the form, adds the
        # 'email' field to the default fields
        fields = UserCreationForm.Meta.fields + ("email",)
