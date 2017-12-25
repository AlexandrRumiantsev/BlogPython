from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def user_detail(request, pk):
    user = request.user
    #Запрос к бд с параметром author=user
    post = Post.objects.filter(author=user)
    user = get_object_or_404(User, pk=pk)
    return render(request, 'blog/user_detail.html', {'user': user,'post':post})

#Регистрация

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)



