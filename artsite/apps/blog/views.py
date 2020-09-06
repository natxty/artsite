from django.shortcuts import render
from django.http import Http404
from .models import Post
 
def blog_main(request):
	return render(request, "blog/blog_main.html",{
		"posts" : Post.objects.all().order_by('-post_date')
	})
 
def post_specific(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
	except:
		raise Http404
 
	return render(request, "blog/blog_single.html",{
		"post" : p
	})