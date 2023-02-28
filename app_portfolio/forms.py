from django import forms
from django.utils.translation import gettext_lazy as _
from app_portfolio.models import Work


class EditWorkForm(forms.ModelForm):
    price = forms.DecimalField(required=False, label=_('стоимость'),
                               widget=forms.TextInput(attrs={
                                   'data-validate': 'require',
                               }))
    time_spent = forms.IntegerField(required=False, label=_('потрачено времени'),
                               widget=forms.TextInput(attrs={
                                   'data-validate': 'require',
                               }))
    image = forms.ImageField(required=False, label=_('обложка'),
                              widget=forms.ClearableFileInput(attrs={
                                  'type': 'file',
                                  'accept': '.jpg, .png',
                                  'data-validate': 'onlyImgAvatar',
                              }))

    class Meta:
        model = Work
        fields = ('title', 'description', 'image', 'price', 'price_currency', 'time_spent', 'time_type', 'link',
                  'video', 'category', 'is_active', 'ordering', 'file1', 'file2', 'file3', 'file4')
        widgets = {
            'ordering': forms.RadioSelect,
            # 'category': forms.Select,
        }


class CreateWorkForm(forms.ModelForm):
    price = forms.DecimalField(required=False, label=_('стоимость'),
                               widget=forms.TextInput(attrs={
                                   'data-validate': 'require',
                               }))
    time_spent = forms.IntegerField(required=False, label=_('потрачено времени'),
                               widget=forms.TextInput(attrs={
                                   'data-validate': 'require',
                               }))
    image = forms.ImageField(required=False, label=_('обложка'),
                              widget=forms.ClearableFileInput(attrs={
                                  'type': 'file',
                                  'accept': '.jpg, .png',
                                  'data-validate': 'onlyImgAvatar',
                              }))

    class Meta:
        model = Work
        fields = ('title', 'description', 'image', 'price', 'price_currency', 'time_spent', 'time_type', 'link',
                  'video', 'category', 'is_active', 'ordering', 'file1', 'file2', 'file3', 'file4')
        widgets = {
            'ordering': forms.RadioSelect,
            # 'category': forms.Select,
        }
