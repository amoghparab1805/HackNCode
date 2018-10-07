from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import requests
import json
from .models import Post
from django.utils import timezone
from .forms import PostForm

def HomePage(request):
	return render(request, 'front_page.html')  

'''def SignUp(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('MentalHealthAwareness:login')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form':form}) 
'''
def Quotes(request):
	return render(request, 'quotes.html')

def Help(request):
	return render(request, 'help.html')

def Videos(request):
	return render(request, 'videos.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_remove(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.delete()
	return redirect('post_list')