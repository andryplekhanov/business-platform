from django import template
import re
register = template.Library()


@register.filter()
def replace_vars(text, user):
    VARS = {
        '{$email}': user.email,
        '{$full_name}': user.full_name,
        '{$phone_number}': user.phone_number,
        '{$date_joined}': user.date_joined.strftime('%d.%m.%Y'),
    }
    variables = re.findall(r'{\$\w+}', text)
    for variable in variables:
        text = text.replace(variable, VARS[variable] if VARS[variable] != '' else 'NoData')
    return text
