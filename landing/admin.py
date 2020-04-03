from django.contrib import admin
from .models import *


class SubAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ('name',)
    fields = ["email", ]
    search_fields = ["name", "email", ]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubAdmin)
