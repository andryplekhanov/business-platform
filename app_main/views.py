from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'app_main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
