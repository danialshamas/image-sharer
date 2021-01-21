# from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView
from django.contrib import messages
from .models import Feed_post
from .forms import PostForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'feed/home.htm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Feed_post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = 'feed/detail.htm'
    model = Feed_post

class AddPostView(FormView):
    template_name = 'feed/new_post.htm'
    form_class = PostForm
    success_url ="/" # go back to the home page

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        new_object = Feed_post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image'],
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your Post was Successfull ')
        return super().form_valid(form)