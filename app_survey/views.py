from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView

from app_survey.models import Question, Choice, Answer

User = get_user_model()


class PollListView(ListView):
    model = Question
    extra_context = {
        'title': _('Новости'), 'current_elem': 'polls-list',
        'breadcrumbs': {_('Главная'): 'home', _('Все голосования'): 'polls-list'}
    }

    def get_queryset(self):
        queryset = Question.objects.filter(visible=True, pub_date__lte=timezone.now()).only('id', 'title', 'pub_date', 'end_date')
        return queryset


class PollDetailView(DetailView):
    model = Question
    extra_context = {
        'title': _('Новости'), 'current_elem': 'polls-detail',
        'breadcrumbs': {_('Главная'): 'home', _('Все голосования'): 'polls-list', _('Голосование'): 'polls-detail'}
    }

    def get_queryset(self):
        queryset = Question.objects.filter(id=self.kwargs.get('pk'), visible=True, pub_date__lte=timezone.now())
        return queryset

    def get(self, request, *args, **kwargs):
        question = self.get_object()
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse('polls-results', args=(kwargs.get('pk'),)))
        if question.end_date < timezone.now() or not self.request.user.paid_entrance_fee:
            return HttpResponseRedirect(reverse('polls-results', args=(kwargs.get('pk'),)))
        try:
            answer = self.request.user.answer_set.get(question=question)
        except ObjectDoesNotExist:
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('polls-results', args=(kwargs.get('pk'),)))

    # def get_context_data(self, **kwargs):
    #     context = super(PollDetailView, self).get_context_data(**kwargs)
    #     return context


class PollResultsView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'app_survey/question_results.html'
    extra_context = {
        'title': _('Новости'), 'current_elem': 'polls-results',
        'breadcrumbs': {_('Главная'): 'home', _('Все голосования'): 'polls-list', _('Результаты голосования'): 'polls-results'}
    }

    def get_context_data(self, **kwargs):
        context = super(PollResultsView, self).get_context_data(**kwargs)
        question = self.get_object()
        try:
            context['users_answer'] = self.request.user.answer_set.get(question=question)
        except ObjectDoesNotExist:
            context['users_answer'] = None
        context['total_partners'] = User.objects.filter(paid_entrance_fee=True, date_joined__lt=question.end_date).count()
        return context


@login_required
def vote(request, question_id):
    if not request.user.paid_entrance_fee:
        raise PermissionDenied
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer = request.user.answer_set.get(question=question)
    except ObjectDoesNotExist:
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'app_survey/question_detail.html', {
                'question': question,
                'error_message': _("Вы не проголосовали."),
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            Answer.objects.create(user=request.user, question=question, choice=selected_choice)
    return HttpResponseRedirect(reverse('polls-results', args=(question.id,)))
