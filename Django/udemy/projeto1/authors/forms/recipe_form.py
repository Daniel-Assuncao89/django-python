from collections import defaultdict
from django import forms
from django.core.exceptions import ValidationError
from recipes.models import Recipe
from utils.strings import is_positive_number


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Recipe
        fields = (
            'title',
            'description',
            'preparation_time',
            'preparation_time_unit',
            'servings',
            'servings_unit',
            'preparation_steps',
            'cover'
        )
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Porções', 'Porções'),
                    ('Pedaços', 'Pedaços'),
                    ('Pessoas', 'Pessoas'),
                )
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Horas', 'Horas'),
                    ('Minutos', 'Minutos')
                )
            )
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data

        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        preparation_steps = cleaned_data.get('preparation_steps')

        if len(title) < 5:
            self._my_errors['title'].append('Must have at least 5 chars')

        if title == description:
            self._my_errors['title'].append('Cannot be equal to description')
            self._my_errors['description'].append('Cannot be equal to title')

        if len(preparation_steps) < 100:
            self._my_errors['preparation_steps'].append(
                'Must have at least 100 caracters'
            )

        if not is_positive_number(cleaned_data.get('preparation_time')):
            self._my_errors['preparation_time'].append(
                'Must be a positive number'
            )

        if not is_positive_number(cleaned_data.get('servings')):
            self._my_errors['servings'].append(
                'Must be a positive number'
            )

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean
