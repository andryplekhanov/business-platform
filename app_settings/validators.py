from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


def icon_size_validate(value):
    """ Валидатор. Проверяет размер загружаемого изображения """
    image_size = value.size
    max_megabytes = 1.0
    if image_size > max_megabytes * 1024 * 1024:
        raise ValidationError(_(f"Ошибка загрузки: допускается размер файла не более {max_megabytes} MB"))


# Валидатор. Проверяет формат загружаемого изображения
icon_validator = FileExtensionValidator(
        allowed_extensions=['png', 'svg'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .png .svg')
    )
