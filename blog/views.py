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

#Функция для добавления новых публикаций
def newPublication(request):
    form = PostForm()
    ctx = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save()
            ctx = {'obj': obj}
    ctx.update({'form': form})


    return render(request, 'blog/send_post.html', ctx)


# Регистрация

from django.views.generic.edit import FormView, FormView, FormView
from django.contrib.auth.forms import UserCreationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # send_mail()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
