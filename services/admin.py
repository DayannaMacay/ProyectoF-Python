from django.contrib import admin
from .models import Service, Testimony

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Service, ServiceAdmin)

class TestimonyAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Testimony, TestimonyAdmin)