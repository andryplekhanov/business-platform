from django import template
import re
register = template.Library()


def get_users_data(user, variable):
    if not user.is_authenticated:
        return variable
    VARS = {
        '{$email}': user.email,
        '{$first_name}': user.first_name,
        '{$username}': user.username,
        '{$last_name}': user.last_name,
        '{$patronymic}': user.patronymic,
        '{$phone_number}': user.phone_number,
        '{$date_joined}': user.date_joined.strftime('%d.%m.%Y'),
        '{$country}': user.country,
        '{$address}': user.address,
        '{$personal_number}': user.personal_number,
        '{$document_number}': user.document_number,
        '{$document_issued}': user.document_issued,
        '{$bank_name}': user.bank_name,
        '{$bank_address}': user.bank_address,
        '{$bank_bic}': user.bank_bic,
        '{$bank_correspondent_account}': user.bank_correspondent_account,
        '{$payment_account}': user.payment_account,
        '{$recipients_name}': user.recipients_name,
    }

    if VARS[variable] == '' or VARS[variable] is None:
        return 'None'
    return VARS[variable]


@register.filter()
def replace_vars(text, user):
    variables = re.findall(r'{\$\w+}', text)
    for variable in variables:
        text = text.replace(variable, get_users_data(user, variable))
    return text
