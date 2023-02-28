from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'app_users/profile/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        _('Подтвердите регистрацию'),
        message,
        to=[user.email],
    )
    email.send()


def get_referrer(url_str):
    try:
        referrers_id = int(str(url_str)[6:])
        referrers_date = str(url_str)[:6]
        referrer = User.objects.get(id=referrers_id)
        if referrer.date_joined.strftime('%y%m%d') == referrers_date:
            return referrer
        return None
    except ObjectDoesNotExist:
        return None
