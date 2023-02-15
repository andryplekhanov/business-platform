from django.contrib import admin
from .models import Question, Answer, Choice
from django.utils.translation import gettext_lazy as _


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'visible', 'pub_date', 'end_date')
    list_filter = ('pub_date', 'end_date', 'visible', )
    readonly_fields = ['get_result', ]
    inlines = [ChoiceInline]
    save_on_top = True

    def get_result(self, obj):
        return 'здесь будет результат'
    get_result.short_description = _('результат')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', )
    list_filter = ('user__email', 'question__title')
    search_fields = ('user__full_name', 'user__email', 'question__title')
    readonly_fields = ['user', 'question', 'choice']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
