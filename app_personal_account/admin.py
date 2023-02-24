from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from app_personal_account.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'get_personal_account', 'balance_before', 'amount', 'direction', 'reason', 'datetime', 'balance_after')
    list_filter = ('direction', 'reason')
    search_fields = ('user__email', 'user__last_name' )
    readonly_fields = ('balance_before', 'balance_after', 'exist')

    def get_user(self, obj):
        link = reverse("admin:app_users_customuser_change", args=[obj.user_id])
        return format_html('<a href="{}">{}</a>', link, obj.user)
    get_user.short_description = _('пользователь')

    def get_personal_account(self, obj):
        return obj.user.personal_account
    get_personal_account.short_description = _('лицевой счет')


admin.site.register(Transaction, TransactionAdmin)
