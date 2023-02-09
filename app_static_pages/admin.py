from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from .models import *


class StaticPageInline(admin.StackedInline):
    model = StaticPage
    verbose_name = "Содержание"


class StaticPageAdmin(FlatPageAdmin):
    inlines = [StaticPageInline]
    fieldsets = (
        (None, {'fields': ('url', 'title', 'sites')}),
        (('Advanced options'), {
            'fields': ('template_name', 'registration_required'),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')
    save_on_top = True


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, StaticPageAdmin)
