from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):  # чтобы в админке отобразить древовидную структуру, нужно унаследовать от DjangoMpttAdmin
    list_display = ('id', 'email', 'full_name', 'get_referer', 'is_verified', 'is_freelancer', 'can_invite_referrals', 'date_joined')
    list_filter = ('date_joined', 'is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')
    # fieldsets = (
    #     (None, {'fields': ('email', 'full_name', 'password', 'phone_number', 'avatar', 'date_joined')}),
    #     (_('Разрешения'), {'fields': ('is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')}),
    #     (_('Реферальная система'), {'fields': ('parent', 'get_level_1_referrals', 'get_level_2_referrals', 'get_level_3_referrals', 'referral_url')}),
    # )

    search_fields = ('id', 'email', 'full_name', 'parent__full_name', 'parent__email')
    readonly_fields = ['date_joined', 'get_level_1_referrals', 'get_level_2_referrals', 'get_level_3_referrals', 'referral_url']
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

    def get_level_1_referrals(self, obj):
        return obj.level_1_referrals.count()
    get_level_1_referrals.short_description = _('рефералов 1го уровня')

    def get_level_2_referrals(self, obj):
        return obj.level_2_referrals.count()
    get_level_2_referrals.short_description = _('рефералов 2го уровня')

    def get_level_3_referrals(self, obj):
        return obj.level_3_referrals.count()
    get_level_3_referrals.short_description = _('рефералов 3го уровня')

    def get_referer(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.parent_id])
        return format_html('<a href="{}">{}</a>', link, obj.parent)
    get_referer.short_description = _('реферер')


admin.site.register(CustomUser, CustomUserAdmin)
