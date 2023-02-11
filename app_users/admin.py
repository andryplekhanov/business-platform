from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('id', 'email', 'full_name', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals', 'date_joined')
    list_filter = ('date_joined', 'is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password', 'phone_number', 'avatar', 'date_joined')}),
        (_('Разрешения'), {'fields': ('is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_verified', 'is_freelancer', 'can_invite_referrals')}
         ),
    )
    search_fields = ('id', 'email', 'full_name')
    ordering = ('-id',)
    readonly_fields = ['date_joined']
    save_on_top = True
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_active.short_description = _('активировать')
    make_inactive.short_description = _('деактивировать')


admin.site.register(CustomUser, CustomUserAdmin)
