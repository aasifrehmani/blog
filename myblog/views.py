from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPosts, Comments
from .forms import BlogPostForm, CommentForm

# Create your views here.
def index(request):
	blogPosts 	=	BlogPosts.objects.order_by('id')
	context 	=	{'posts':blogPosts}
	return render(request, 'home.html', context)

def add(request):
	if request.method == 'POST':
		frm_post =	BlogPostForm(request.POST)

		if frm_post.is_valid():
			frm_post.save()
			return redirect('index')

		return render(request, 'index.html')
	else:
		frm_post =	BlogPostForm()
		context		=	{'frm_post':frm_post}
		return render(request, 'add_post.html', context)

def view(request, postid):
	frm_post		=	BlogPosts.objects.get(pk=postid)

	if request.method == 'POST':
		insert_comment	=	CommentForm(request.POST)
		if insert_comment.is_valid():
			temp 	=	insert_comment.save(commit=False)
			temp.postid 	=	frm_post
			temp.save()

	frm_comments	=	CommentForm()
	context 		=	{'frm_post':frm_post, 'frm_comments':frm_comments}

	return render(request, 'view_post.html', context)

def edit(request, postid):
	blogPost 	=	BlogPosts.objects.get(pk=postid)

	if request.method == 'POST':
		frm_post 	=	BlogPostForm(request.POST, instance = blogPost)
		if frm_post.is_valid():
			frm_post.save()
			return redirect('view')

	else:
		frm_post 	=	BlogPostForm(instance = blogPost)

		context 	=	{'frm_post':frm_post}
		return render(request, 'edit_post.html', context)

def delete(request, postid):
	blogPost 	=	BlogPosts.objects.get(pk=postid)

	if request.method == 'POST':
		blogPost.delete()
		return redirect('index')
	else:
		context 	=	{'blogPost':blogPost}
		return render(request, 'delete_post.html',context)