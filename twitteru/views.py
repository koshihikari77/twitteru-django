from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import login
from .forms import SignupForm
from django.views.generic import CreateView

from .models import User, Post, Like

# Create your views here.


class UserPageView(generic.DetailView):
    model = User
    template_name = "twitteru/user_page.html"


"""
def user_page(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = user.select_related()
    return render(request, 'twitteru/user_page.html', {'user': user,
                                                       'posts': posts})
"""


class PostPageView(generic.DetailView):
    model = Post
    template_name = "twitteru/user_page.html"


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
        return redirect(request.META['HTTP_REFERER'])
        # like
    post.liked_num += 1
    post.save()
    like = Like()
    like.user = request.user
    like.post = post
    like.save()
    return redirect(request.META['HTTP_REFERER'])


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # バリデーションが通ったあとの処理を記述
        # self.objectにsave()されたユーザーオブジェクトが格納される
        # 独自処理を終えたら継承元のメソッドに処理を渡す
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


"""
def toppage:

def follow:

class HomePageView(generic.DetailView):

class TweetView(generic.DetailView):

class SearchResultView(generic.ListView):

class UserSettingView(generic.DetailView):
"""
