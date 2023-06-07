from django import forms

CHOICE_STATUS = (
    ('PR', 'Priority'),
    ('AT', 'Attention'),
    ('GR', 'Green')
)


class TaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=250)
    status = forms.ChoiceField(choices=CHOICE_STATUS)
