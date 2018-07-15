from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category, Discussion,Comment
from .forms import DiscussionForm, CommentForm
from django.utils import timezone

def index(request):
    category_list = Category.objects.all
    context = {"category_list": category_list}
    return render(request, 'index.html', context)

def detail(request, category_id):    
    obj = Category.objects.get(pk = category_id)    
    form = DiscussionForm() 
    discussion_list = Discussion.objects.filter(category_id = category_id)   
    context = {"category_text": obj, "form": form,"discussion_list": discussion_list}
    return render(request, 'detail.html',context)

def InsertDiscussion(request, category_id):
    discussion_list = Discussion.objects.filter(category_id=category_id)
    obj = Category.objects.get(pk = category_id)
    if request.method == 'POST':
        formT = DiscussionForm(request.POST)
        if formT.is_valid():
            d = formT.cleaned_data['discussion']
            p = Discussion(category_id=category_id, discussion_text=d,pub_date=timezone.now())
            p.save()
    form = DiscussionForm()      
    context = {"category_text": obj, "form": form,"discussion_list": discussion_list }   
    return render(request, 'detail.html', context)  

def comment(request, discussion_id):    
    obj = Discussion.objects.get(pk = discussion_id)
    form = CommentForm()   
    comment_list = Comment.objects.filter(discussion_id=discussion_id)
    context = {"discussion_text": obj, "form": form, "comment_list": comment_list}
    return render(request, 'comment.html',context)

def InsertComment(request, discussion_id):
    comment_list = Comment.objects.filter(discussion_id=discussion_id)
    obj =Discussion.objects.get(pk = discussion_id)
    if request.method == 'POST':
        formT = CommentForm(request.POST)
        if formT.is_valid():
            d = formT.cleaned_data['comment']
            p = Comment(discussion_id=discussion_id, comment_text=d,pub_date=timezone.now())
            p.save()
    form = CommentForm()      
    context = {"discussion_text": obj, "form": form,"comment_list": comment_list }   
    return render(request, 'comment.html', context)    