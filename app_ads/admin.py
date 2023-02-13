from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils.translation import gettext_lazy as _
from app_ads.models import Category, Adv


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AdvAdmin(admin.ModelAdmin):
    list_display = ['created', 'link_to_author', 'get_short_title', 'category', 'price', ]
    list_filter = ['created', ]
    search_fields = ['author__full_name', 'author__email', 'author__phone_number', 'title']
    save_on_top = True
    ordering = ['-created']

    def link_to_author(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.author_id])
        return format_html('<a href="{}">{}</a>', link, obj.author.email)
    link_to_author.short_description = _('автор')

    def get_short_title(self, obj):
        if len(obj.title) <= 50:
            return obj.title
        return f'{obj.title[:50]}...'
    get_short_title.short_description = _('заголовок')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Adv, AdvAdmin)
