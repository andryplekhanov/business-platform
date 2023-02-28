from django.contrib import admin
from .models import Question, Answer, Choice
from django.utils.translation import gettext_lazy as _


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ['votes', ]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'pub_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('pub_date', 'end_date', 'visible', )
    readonly_fields = ['get_result', ]
    inlines = [ChoiceInline]
    save_on_top = True

    def get_result(self, obj):
        return 'здесь можно установить вывод результата'
    get_result.short_description = _('результат')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', )
    search_fields = ('user__full_name', 'user__email', 'question__title')
    readonly_fields = ['user', 'question', 'choice']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer, AnswerAdmin)
