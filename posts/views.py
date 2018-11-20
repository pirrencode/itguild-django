from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body']:
            post = Post()
            post.title = request.POST['title']
            post.body = request.POST['body']
            post.image = request.FILES['image']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect("home")
        else:
            return render(request, 'posts/create.html', {'error':'ERROR: you must include a title and URL to create a post!'})
    else:
        return render(request, 'posts/create.html')

def home(request):
    post = Post.objects.order_by('-votes_total')
    return render(request, 'posts/home.html', {'posts':post})

def gallery(request):
    return render(request, 'posts/gallery.html')

def about(request):
    return render(request, 'posts/about.html')

def rss(request):
    return render(request, 'posts/rss.html')

def manifesto(request):
    return render(request, 'posts/manifesto.html')

def upvote(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        #post = Post.object.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect("home")

def downvote(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        #post = Post.object.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect("home")

def userposts(request, fk):
    posts = Post.objects.filter(author__id=fk).order_by('-votes_total')
    author = get_object_or_404(User, pk=fk)
    return render(request, 'posts/userposts.html', {'posts':posts, 'author':author})
