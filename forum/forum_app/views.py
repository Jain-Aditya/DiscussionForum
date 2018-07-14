from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category, Discussion


def index(request):
    category_list = Category.objects.all
    context = {"category_list": category_list}
    return render(request, 'index.html', context)
    Category.category_text
def detail(request, category_id):
    obj = Category.objects.get(pk = category_id)
    context = {"category_text": obj}
    return render(request, 'detail.html',context)
