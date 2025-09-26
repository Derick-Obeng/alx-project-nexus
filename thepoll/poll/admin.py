from django.contrib import admin

# Register your models here.
from .models import Choice, Poll

admin.site.register(Choice)
admin.site.register(Poll)
