from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import ExpenseInfo
from django.contrib.auth.models import User
from django.db.models import Sum
import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Q
# Create your views here.


def index(request):
    expense_items = ExpenseInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        budget_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
        expense_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(expenses=Sum('cost',filter=Q(cost__lt=0)))
        fig,ax=plt.subplots()
        ax.bar(['Expenses','Budget'], [abs(expense_total['expenses']),budget_total['budget']],color=['red','green'])
        ax.set_title('Your total expenses vs total budget')
        plt.savefig('budget/static/budget/expense.jpg')
    except TypeError:
        print('No data.')
    context = {'expense_items':expense_items,'budget':budget_total['budget'],'expenses':expense_total['expenses']}
    return render(request,'budget/index.html',context=context)

def add_item(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    ExpenseInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    budget_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
    expense_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(expense=Sum('cost',filter=Q(cost__lt=0)))
    fig,ax=plt.subplots()
    ax.bar(['Expenses','Budget'], (expense_total['expense'], budget_total['budget']), color=['red','green'])
    ax.set_title('Your total expenses vs. total budget')
    plt.savefig('budget/static/budget/expense.jpg')
    return HttpResponseRedirect('/budget/app')