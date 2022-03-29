from django.contrib.auth.models import User
from django.urls import reverse_lazy
from post import forms, models
from django.views import generic
from django.shortcuts import render 

# Create your views here.
class PostList(generic.ListView):
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_pg'] = 'Lista de Post'
        return context

class PostDetail(generic.DetailView):
    model = models.Post

class CreatePost(generic.CreateView):
    model = models.Post
    fields = '__all__'
    success_url = reverse_lazy('post:home')

    """
    def get_success_url(self):
        return reverse('post:home')
    """

class UpdatePost(generic.UpdateView):
    pass

class DeletePost(generic.DeleteView):
    pass

class NuevoUser(generic.CreateView):
    model = User
    template_name = 'registration/registro.html'
    form_class = forms.RegistroForm
    success_url = reverse_lazy('login')
    