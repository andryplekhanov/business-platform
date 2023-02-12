from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals', 'date_joined')
    list_filter = ('date_joined', 'is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password', 'phone_number', 'avatar', 'date_joined')}),
        (_('Разрешения'), {'fields': ('is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')}),
        (_('Реферальная система'), {'fields': ('referer', 'get_referrals')}),
    )

    search_fields = ('id', 'email', 'full_name')
    readonly_fields = ['date_joined', 'get_referrals']
    save_on_top = True
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = _('активировать')

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = _('деактивировать')

    def get_referrals(self, obj):
        return CustomUser.objects.filter(referer_id=obj.id).count()

    get_referrals.short_description = _('пригласил пользователей')


admin.site.register(CustomUser, CustomUserAdmin)
