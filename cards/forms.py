# cards/forms.py

from django import forms
from .models import Category

class CardForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    answer = forms.CharField(label='Ответ', widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, "class": "form-control"}), max_length=5000)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), 
                                      label='Категория', empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={"class": "form-control"}))