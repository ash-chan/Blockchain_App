from django.contrib import admin

from .models import Mentor, Mentee

class MentorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name']}),
        (None,                  {'fields': ['join_date']}),
        (None,                  {'fields': ['profession']}),
        (None,                  {'fields': ['inv_usd']}),
        (None,                  {'fields': ['inv_zco']}),
    ]

class MenteeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name']}),
        (None,                  {'fields': ['join_date']}),
        (None,                  {'fields': ['major']}),
        (None,                  {'fields': ['grad_date']}),
    ]

admin.site.register(Mentor, MentorAdmin)


admin.site.register(Mentee, MenteeAdmin)


