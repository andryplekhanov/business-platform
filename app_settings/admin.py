from django.contrib import admin

from app_settings.models import ContactSettings, ContactGrop, CompanySettings, FooterPagesSet, FooterPagesLeftSet


class ContactGropInline(admin.TabularInline):
    model = ContactGrop


class ContactSettingsAdmin(admin.ModelAdmin):
    """ В админ-панели нужно создать экземпляр с настройками """

    inlines = [ContactGropInline]

    def has_add_permission(self, request, obj=None):
        """ Запрещает создать более 1го экземпляра с настройками """
        if not self.model.objects.all():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """ Запрещает удалять экземпляр с настройками """
        return False


class FooterPagesSetAdmin(admin.ModelAdmin):
    """ В админ-панели нужно создать экземпляр с настройками """

    def has_add_permission(self, request, obj=None):
        """ Запрещает создать более 1го экземпляра с настройками """
        if not self.model.objects.all():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """ Запрещает удалять экземпляр с настройками """
        return False


class FooterPagesLeftSetAdmin(admin.ModelAdmin):
    """ В админ-панели нужно создать экземпляр с настройками """

    def has_add_permission(self, request, obj=None):
        """ Запрещает создать более 1го экземпляра с настройками """
        if not self.model.objects.all():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """ Запрещает удалять экземпляр с настройками """
        return False


class CompanySettingsAdmin(admin.ModelAdmin):
    """ В админ-панели нужно создать экземпляр с настройками """

    def has_add_permission(self, request, obj=None):
        """ Запрещает создать более 1го экземпляра с настройками """
        if not self.model.objects.all():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """ Запрещает удалять экземпляр с настройками """
        return False


admin.site.register(ContactSettings, ContactSettingsAdmin)
admin.site.register(CompanySettings, CompanySettingsAdmin)
admin.site.register(FooterPagesSet, FooterPagesSetAdmin)
admin.site.register(FooterPagesLeftSet, FooterPagesLeftSetAdmin)
