from django import forms
from .questions.answer import Answer
from .const import AGREE_LEVELS


class AnswersForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.RadioSelect(
        choices=AGREE_LEVELS))

    class Meta:
        model = Answer
        fields = ['answer']

