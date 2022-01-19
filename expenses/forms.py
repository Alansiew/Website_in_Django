import django_filters
from django import forms

from .models import Expense


class ExpenseCategorySearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False


class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False


class ExpenseAmountSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].required = False


class ExpenseDateSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d','%Y.%m.%d','%Y/%m/%d','%d-%m-%Y','%d.%m.%Y','%d/%m/%Y']
        self.fields['date'].required = False


# Data searcher method

class ExpenseFilter(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('category',)
