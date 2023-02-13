from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'get_referer', 'is_verified', 'is_freelancer', 'can_invite_referrals', 'date_joined')
    list_filter = ('date_joined', 'is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password', 'phone_number', 'avatar', 'date_joined')}),
        (_('Разрешения'), {'fields': ('is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')}),
        (_('Реферальная система'), {'fields': ('referer', 'get_referrals', 'referral_url')}),
    )

    search_fields = ('id', 'email', 'full_name')
    readonly_fields = ['date_joined', 'get_referrals', 'referral_url']
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
        return CustomUser.objects.filter(referer_id=obj.id).count()
    get_referrals.short_description = _('пригласил пользователей')

    def get_referer(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.referer_id])
        return format_html('<a href="{}">{}</a>', link, obj.referer)
    get_referer.short_description = _('реферер')


admin.site.register(CustomUser, CustomUserAdmin)
