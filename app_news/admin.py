from django.contrib import admin
from app_news.models import News, NewsLink
from django.utils.translation import gettext_lazy as _


class NewsLinkInline(admin.TabularInline):
    model = NewsLink


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'visible', 'pub_date', 'created')
    search_fields = ('title', 'text')
    list_filter = ('pub_date', 'created', 'visible', 'for_all', 'for_registered', 'for_contractors', 'for_freelancers',
                   'for_new_freelancers', 'for_new_contractors', 'for_core')
    inlines = [NewsLinkInline]
    save_on_top = True
    actions = ['public', 'unpublic']

    def public(self, request, queryset):
        queryset.update(visible=True)
    public.short_description = _('опубликовать')

    def unpublic(self, request, queryset):
        queryset.update(visible=False)
    unpublic.short_description = _('снять с публикации')


admin.site.register(News, NewsAdmin)
