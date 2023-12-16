Changing passwords
-----------------------------------------------------------------------------------------------------------------------
Django does not store raw (clear text) passwords on the user model, but only a hash

1. By Using manage.py
-----------------------------------------------------------
python manage.py changepassword "nshankar"

2. Using Shell to change password programmatically
-----------------------------------------------------------
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username="john")
>>> u.set_password("new password")
>>> u.save()