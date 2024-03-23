from django import forms
from .models import Patient


class FormChoice(forms.Form):
    total_models = Patient.objects.count()
    interval = total_models // 2
    options = []
    for i in range(5):
        start = i * interval
        end = start + interval
        if start == 0:
            start = 1
            option = f"{start}-{end}"
            options.append((option, option))
        else:
            option = f"{start}-{end}"
            options.append((option, option))
    select = forms.ChoiceField(choices=options, widget=forms.Select(attrs={'id': 'mon_select'}))
    search_time = forms.CharField(label='Search', required=False, max_length=100,
                                  widget=forms.TextInput(attrs={'id': 'search_time', 'placeholder': 'By Date'}))
