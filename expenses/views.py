from django.views.generic.list import ListView
from .forms import ExpenseSearchForm, ExpenseCategorySearchForm, ExpenseAmountSearchForm, ExpenseDateSearchForm
from .models import Expense, Category
from .reports import summary_per_category,summary_per_id


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5


    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        category_form = ExpenseCategorySearchForm(self.request.GET)
        form = ExpenseSearchForm(self.request.GET)
        amount_form = ExpenseAmountSearchForm(self.request.GET)
        date_specific=ExpenseDateSearchForm(self.request.GET)
        date_from = self.request.GET.get('fromdate') ##it get value of first date of the date choicer##
        date_to = self.request.GET.get('todate')##it get value of second date of the date choicer##


        ## below the query methods for 
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

        if category_form.is_valid():
            category = category_form.cleaned_data.get('category', '')
            if category:
                queryset = queryset.filter(category__name=category)

        if amount_form.is_valid():
            amount = amount_form.cleaned_data.get('amount', '')
            if amount:
                queryset = queryset.filter(amount__lte=amount)

        if date_specific.is_valid():
            dateSpecific = date_specific.cleaned_data.get('date','')
            if dateSpecific:
                queryset = queryset.filter(date__icontains=dateSpecific)
        if date_from:
            queryset = queryset.filter(date__range=(date_from,date_to))

        queryset = queryset.order_by('-date')

        return super().get_context_data(
            form=form,
            date_from=date_from,
            date_to=date_to,
            date_specific=date_specific,
            category_form=category_form,
            amount_form=amount_form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            summary_per_id=summary_per_id(queryset),
            **kwargs)


class CategoryListView(ListView):
    model = Category
    paginate_by = 5