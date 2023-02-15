from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):  # чтобы в админке отобразить древовидную структуру, нужно унаследовать от DjangoMpttAdmin
    list_display = ('id', 'email', 'full_name', 'get_referer', 'status', 'is_core', 'date_joined')
    list_filter = ('date_joined', 'is_staff', 'is_active', 'is_core', 'status')
    search_fields = ('id', 'email', 'full_name', 'parent__full_name', 'parent__email')
    readonly_fields = ['date_joined', 'get_referrals', 'referral_url', 'parent']
    save_on_top = True
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = _('активировать')

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = _('деактивировать')

    def referral_url(self, obj):
        return obj.get_referral_url()
    referral_url.short_description = _('ссылка-приглашение')

    def get_referrals(self, obj):
        referrals = obj.referrals
        return f"1 level: {referrals.get('level1').count()}\n" \
               f"2 level: {referrals.get('level2').count()}\n" \
               f"3 level: {referrals.get('level3').count()}"
    get_referrals.short_description = _('рефералы')

    def get_referer(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.parent_id])
        return format_html('<a href="{}">{}</a>', link, obj.parent)
    get_referer.short_description = _('реферер')


admin.site.register(CustomUser, CustomUserAdmin)
