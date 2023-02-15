from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView

from app_survey.models import Question, Choice, Answer


class PollListView(LoginRequiredMixin, ListView):
    model = Question

    def get_queryset(self):
        queryset = Question.objects.filter(visible=True, pub_date__lte=timezone.now()).only('id', 'title', 'pub_date', 'end_date')
        return queryset


class PollDetailView(LoginRequiredMixin, DetailView):
    model = Question

    def get_queryset(self):
        queryset = Question.objects.filter(id=self.kwargs.get('pk'), visible=True, pub_date__lte=timezone.now())
        return queryset

    def get(self, request, *args, **kwargs):
        question = self.get_object()
        if question.end_date < timezone.now():
            return HttpResponseRedirect(reverse('polls-results', args=(kwargs.get('pk'),)))
        try:
            answer = self.request.user.answer_set.get(question=question)
        except ObjectDoesNotExist:
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('polls-results', args=(kwargs.get('pk'),)))

    # def get_context_data(self, **kwargs):
    #     context = super(PollDetailView, self).get_context_data(**kwargs)
    #     context['poll'].votable = self.object.can_vote(self.request.user)
    #     return context


class PollResultsView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'app_survey/question_results.html'

    def get_context_data(self, **kwargs):
        context = super(PollResultsView, self).get_context_data(**kwargs)
        question = self.get_object()
        try:
            context['users_answer'] = self.request.user.answer_set.get(question=question)
        except ObjectDoesNotExist:
            context['users_answer'] = _('Вы не успели проголосовать')
        context['is_finished'] = question.end_date < timezone.now()
        return context


@login_required
def vote(request, question_id):
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
