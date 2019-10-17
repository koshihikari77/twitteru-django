from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.views.generic import CreateView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils import timezone

from .models import Post, Like, Follow
from .forms import TweetForm, PostForm

# Create your views here.


class UserPageView(generic.DetailView):
    model = get_user_model()
    template_name = "twitteru/user_page.html"


def user_home(request):
    user = request.user
    posts = user.select_related("post")
    return render(request, 'twitteru/user_home.html', {'user': user,
                                                       'posts': posts})


class PostPageView(generic.DetailView):
    model = Post
    template_name = "twitteru/user_page.html"


def tweet(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.posted_date = timezone.now()
            post.liked_num = 0
            post.replayed_num = 0
            post.retweeted_num = 0
            post.replay_flag = False
            post.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = PostForm(request.POST or None)
    return render(request, 'twitteru/form.html', {'form': form})


def follow(request, *args, **kwargs):
    followed_user = get_user_model().objects.get(id=kwargs['pk'])
    is_follow = Follow.objects.filter(
        followed_user=followed_user).filter(following_user=request.user).count()

    if is_follow > 0:
        following = Follow.objects.get(
            followed_user=followed_user, following_user=request.user)
        following.delete()
    else:
        follow = Follow()
        follow.followed_user = followed_user
        follow.following_user = request.user
        follow.save()
    return redirect(request.META['HTTP_REFERER'])


def ajax_like(request, *args, **kwargs):
    post = Post.objects.get(id=kwargs['pk'])
    is_like = Like.objects.filter(user=request.user).filter(post=post).count()
    # unlike

    if is_like > 0:
        liking = Like.objects.get(
            post__id=kwargs['pk'], user=request.user)
        liking.delete()
        post.liked_num -= 1
        post.save()
    else:
        post.liked_num += 1
        post.save()
        like = Like()
        like.user = request.user
        like.post = post
        like.save()
    return redirect(request.META['HTTP_REFERER'])


"""


def toppage:


def follow:


class HomePageView(generic.DetailView):


class TweetView(generic.DetailView):


class SearchResultView(generic.ListView):


class UserSettingView(generic.DetailView):
"""
