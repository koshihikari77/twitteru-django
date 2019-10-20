from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils import timezone

from .models import Post, Like, Follow, Image
from .forms import TweetForm, PostForm

# Create your views here.


class UserPageView(generic.DetailView):
    model = get_user_model()
    template_name = "twitteru/user_page.html"


"""
class UserHomeView(FormView):
    form_class = TweetForm
    template_name = 'user_home.html'
    success_url = redirect(request.META['HTTP_REFERER'])

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        if fomr.is_valid():
"""


def user_home(request, *args, **kwargs):
    user = request.user
    likes = Like.objects.filter(user=user.pk)
    posts = Post.objects.filter(user=user.pk)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():

            post = Post()
            post.user = request.user
            post.text = form.cleaned_data["tweet"]
            post.posted_date = timezone.now()
            post.liked_num = 0
            post.replayed_num = 0
            post.retweeted_num = 0
            post.replay_flag = False
            post.save()

            for image_file in request.FILES.getlist("images"):
                image = Image()
                image.post = post
                image.src = image_file
                image.save()

            return redirect(request.META['HTTP_REFERER'])
    else:
        form = TweetForm(None)
    context = {'user': user, 'posts': posts, 'likes': likes, 'form': form}
    return render(request, 'twitteru/user_home.html', context)


class PostPageView(generic.DetailView):
    model = Post
    template_name = "twitteru/user_page.html"


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


def like(request, *args, **kwargs):
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


def ajax_like(request, *args, **kwargs):
    status = request.GET.getlist('status')
    status = bool(int(status[0]))
    post_id = int(request.GET.get('post_id'))
    user = request.user  # ユーザー情報の取得
    post = Post.objects.get(id=post_id)
    liked = Like.objects.filter(user=user).filter(post=post).count()
    liked = bool(liked)
    if (status):
        if (liked):
            liking = Like.objects.get(post__id=post_id, user=user)
            liking.delete()
            post.liked_num = Like.objects.filter(post=post).count()
            post.save()
        else:
            like = Like()
            like.user = user
            like.post = post
            like.save()
            post.liked_num += Like.objects.filter(post=post).count()
            post.save()

    data = {
        "liked": liked, "liked_num": post.liked_num
    }
    return JsonResponse(data)


"""


def toppage:


def follow:


class HomePageView(generic.DetailView):


class TweetView(generic.DetailView):


class SearchResultView(generic.ListView):


class UserSettingView(generic.DetailView):
"""
