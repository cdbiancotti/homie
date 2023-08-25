from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy   

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

class PostListView(ListView):
    model = Post
    template_name = "blog/pages.html"
    paginate_by=2
    queryset = Post.objects.all().order_by('-date')


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/page.html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_page.html"
    success_url = reverse_lazy('blog:pages')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/update_page.html"
    fields = ['title', 'subtitle', 'body', 'image']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user.username
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('blog:details_page', args=[self.object.id])

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/update_page.html"
    fields = ['title', 'subtitle', 'body', 'image']
    
    def get_success_url(self) -> str:
        return reverse_lazy('blog:details_page', args=[self.object.id])
