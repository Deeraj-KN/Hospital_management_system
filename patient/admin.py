from django.contrib import admin

# Register your models here.
from .models import Hospital, Patient,Department
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Department)