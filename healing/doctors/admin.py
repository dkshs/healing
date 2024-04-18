from django.contrib import admin

from .models import Doctor
from .models import Specialty

admin.site.register(Doctor)
admin.site.register(Specialty)
