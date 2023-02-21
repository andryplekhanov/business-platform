from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from app_news.models import News


class NewsListView(ListView):
    model = News
    extra_context = {
        'title': _('Новости'), 'current_elem': 'news',
        'breadcrumbs': {_('Главная'): 'home', _('Новости'): 'news'}
    }

    def get_queryset(self):

        # Если пользователь - не авторизован, возвращаем новости только из категории "для всех".
        all_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_all=True)
        if self.request.user.is_anonymous:
            return all_queryset.prefetch_related('newslink_set')

        # Для всех авторизованных - новости складываются в список, если чел попадает под условия.
        # Ну а если не попал ни под одно условие, в этом списке уже лежат новости "для всех".
        combined_query = [query_item.id for query_item in all_queryset]

        # Если пользователь - участник ядра
        if self.request.user.is_core:
            core_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_core=True)
            for query_item in core_queryset:
                combined_query.append(query_item.id)

        # Если пользователь - авторизован
        if self.request.user.is_authenticated:
            all_registered_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_registered=True)
            for query_item in all_registered_queryset:
                combined_query.append(query_item.id)

        users_age = timezone.now() - self.request.user.date_joined

        # Если пользователь - заказчик со стажем более 3х месяцев
        if self.request.user.status == "0" and users_age.days > 90:
            all_contractors_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_contractors=True)
            for query_item in all_contractors_queryset:
                combined_query.append(query_item.id)

        # Если пользователь - заказчик со стажем менее 3х месяцев
        if self.request.user.status == "0" and users_age.days <= 90:
            all_new_contractors_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_new_contractors=True)
            for query_item in all_new_contractors_queryset:
                combined_query.append(query_item.id)

        # Если пользователь - фрилансер со стажем более 3х месяцев
        if self.request.user.status == "2" and users_age.days > 90:
            all_freelancers_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_freelancers=True)
            for query_item in all_freelancers_queryset:
                combined_query.append(query_item.id)

        # Если пользователь - фрилансер со стажем менее 3х месяцев
        if self.request.user.status == "2" and users_age.days <= 90:
            all_new_freelancers_queryset = News.objects.filter(visible=True, pub_date__lte=timezone.now(), for_new_freelancers=True)
            for query_item in all_new_freelancers_queryset:
                combined_query.append(query_item.id)

        return News.objects.filter(id__in=combined_query).prefetch_related('newslink_set')
