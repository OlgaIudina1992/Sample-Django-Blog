from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from .models import Post, Category
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    cats = Category.objects.all()
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detailed.html"

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name__contains=cats.lower().replace('-', ' '))
    return render(request, "categories.html", {'cats': cats.upper().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_list = Category.objects.all()
    return render(request, "category_list.html", {'cat_list': cat_list})


