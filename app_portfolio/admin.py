from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from app_portfolio.models import Work


class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_short_title', 'category', 'created_at', 'get_user')
    search_fields = ('user__last_name', 'user__email', 'title', 'category__name')
    readonly_fields = ('user', 'created_at', 'corrected_at')
    list_filter = ('created_at', 'corrected_at')

    def get_short_title(self, obj):
        if len(obj.title) <= 30:
            return obj.title
        return f'{obj.title[:30]}...'
    get_short_title.short_description = 'заголовок'

    def get_user(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.user_id])
        return format_html('<a href="{}">{}</a>', link, obj.user)
    get_user.short_description = _('пользователь')


admin.site.register(Work, WorkAdmin)
