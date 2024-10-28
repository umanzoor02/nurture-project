from django.contrib import admin
from .models import Profile
from .models import Child

admin.site.register(Child)
admin.site.register(Profile)