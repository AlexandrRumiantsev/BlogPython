import datetime

from django.core.mail import send_mail
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, UpdateView

from blog.forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def user_detail(request, pk):
    user = request.user
    # Запрос к бд с параметром author=user
    post = Post.objects.filter(author=user)
    user = get_object_or_404(User, pk=pk)
    return render(request, 'blog/user_detail.html', {'user': user, 'post': post})


# Функция для добавления новых публикаци
from django.http import HttpResponseRedirect


def newPublication(request):
    form = PostForm()
    ctx = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save()
            ctx = {'obj': obj}
            return HttpResponseRedirect('../')

    ctx.update({'form': form})
    return render(request, 'blog/send_post.html', ctx)


def delete(request, pk):
    if request.method == 'POST':
        obj = Post.objects.get(id=pk)
        obj.delete()
    return HttpResponseRedirect('/')


def edit(request, pk):
    if request.method == 'GET':
        massive = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/edit.html', {'massive': massive})


# Регистрация

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/"

    template_name = "register.html"

    def form_valid(self, form):
        # send_mail()
        form.save()

        return super(RegisterFormView, self).form_valid(form)
