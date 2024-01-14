from django.contrib import admin
from .models import Schedule, About

# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields=('hours', 'created', 'updated')
admin.site.register(Schedule, ScheduleAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(About, AboutAdmin)