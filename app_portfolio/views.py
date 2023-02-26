from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from app_portfolio.forms import EditWorkForm, CreateWorkForm
from app_portfolio.models import Work


class PortfolioBest(ListView):
    raise_exception = True
    model = Work
    extra_context = {
        'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_best',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'}
    }

    def get_queryset(self):
        queryset = Work.objects.filter(user=self.request.user, is_active=True).only('title')
        return queryset


class PortfolioBestDetailView(DetailView):
    model = Work
    extra_context = {
        'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_best_detail',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'}
    }


class CreateWorkView(LoginRequiredMixin, CreateView):
    model = Work
    form_class = CreateWorkForm
    template_name = 'app_portfolio/add_work.html'
    success_url = reverse_lazy('portfolio_best')
    extra_context = {
        'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'add_work',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'}
    }

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


class WorkDeleteView(DeleteView):
    model = Work
    success_url = reverse_lazy('portfolio_best')
    template_name = 'app_portfolio/work_confirm_delete.html'


class EditWorkView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Work
    form_class = EditWorkForm
    template_name = 'app_portfolio/edit_work.html'
    extra_context = {
        'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'edit_work',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'}
    }

    def form_valid(self, form):
        messages.info(self.request, _("Работа успешно сохранена"))
        return super(EditWorkView, self).form_valid(form)


def portfolio_current(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_current',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_current.html',
        context=context
    )


def portfolio_rating(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_rating',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_rating.html',
        context=context
    )


def portfolio_reviews(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_reviews',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_reviews.html',
        context=context
    )


def portfolio_settings(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_settings',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_settings.html',
        context=context
    )
