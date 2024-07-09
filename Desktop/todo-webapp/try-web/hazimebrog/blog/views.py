from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Review

from django.urls import reverse, reverse_lazy

from .forms import PostForm

from django.views.generic import CreateView, DetailView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin



def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts":posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    review = Review.objects.filter(book=post) 
    return render(request, "blog/post_detail.html", {"post": post,"review":review})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})




class CreateReviewView(CreateView):
    model = Review
    fields = ('book','title', 'text','rate')
    template_name = 'blog/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Post.objects.get(pk=self.kwargs['blog_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('frontpage')
    
class DeleteBlogView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('frontpage')
    model = Post
    template_name = 'blog/blog_confirm_delete.html'
        

# Create your views here.
