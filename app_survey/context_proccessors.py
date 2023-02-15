from app_survey.models import Question
from django.utils import timezone


def load_number_polls(request):
    if request.user.is_authenticated and request.user.is_core:
        new_polls = Question.objects.exclude(choice__answer__user_id=request.user.id)\
            .filter(visible=True, end_date__gte=timezone.now(), pub_date__lte=timezone.now()).only('id')
        return {
            'number_polls': new_polls.count(),
            'new_polls': new_polls,
        }
    return {
        'number_polls': 0
    }
