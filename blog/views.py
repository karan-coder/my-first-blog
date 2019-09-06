# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
# Create your views here.

	posts = Post.objects.filter(published_date=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
