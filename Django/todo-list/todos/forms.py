from django import forms
from .models import Todo

CHOICE_STATUS = (
    ('PR', 'Priority'),
    ('AT', 'Attention'),
    ('GR', 'Green')
)


class TaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=250)
    status = forms.ChoiceField(choices=CHOICE_STATUS)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = ['task', 'status']
        fields = '__all__'
        widgets = {
            'task': forms.Textarea()
        }
        labels = {
            'task': 'Tarefa',
            'status': 'Prioridade'
        }
        # help_texts = {
        #     'task': 'Aqui você digita a sua tarefa'
        # }
    class Media:
        css = {'all': ('style.css',)}
