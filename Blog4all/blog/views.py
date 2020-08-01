from django.shortcuts import render,get_object_or_404,redirect

from django.utils import timezone
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from blog.models import Blogpost,Comment
from blog.forms import BlogpostForm,CommentForm

from django.contrib.auth.decorators import login_required # used for function views
from django.contrib.auth.mixins import LoginRequiredMixin # used for class based views

from django.urls import reverse_lazy

from django.http import Http404
# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class BlogpostListView(ListView):
    model = Blogpost

    template_name = 'blog/post_list.html'

    def get_queryset(self):     # __lte -> less than or equal to
        return Blogpost.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
                                                                    # - for descending order 

class FilterView(ListView):
    model = Blogpost
    template_name = 'blog/post_list.html'
    def get_queryset(self):
        return Blogpost.objects.filter(topic=self.kwargs['topic_name']).filter(published_date__lte=timezone.now()).order_by('-published_date')

class BlogpostDetailView(DetailView):
    model = Blogpost
    template_name = 'blog/post_detail.html'

class CreateBlogpostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = BlogpostForm

    model = Blogpost
    template_name = 'blog/post_form.html'


class UpdateBlogpostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = BlogpostForm

    model = Blogpost
    template_name = 'blog/post_form.html'

class DeleteBlogpostView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Blogpost
    success_url = reverse_lazy('blog:blogs_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Blogpost
    context_object_name = 'blogpost_list'
    template_name = 'blog/post_draft_list.html'
    def get_queryset(self):
        return Blogpost.objects.filter(published_date__isnull = True).order_by('create_date')


@login_required
def publish_post(request,pk):
    post = get_object_or_404(Blogpost,pk = pk)
    post.publish()
    return redirect('blog:blog_details',pk = pk)



######################
 ## DEAL WITH COMMENTS NOW ##
######################


def adding_comment(request,pk):
    current_post = get_object_or_404(Blogpost,pk = pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = current_post
            comment.save()
            return redirect('blog:blog_details',pk = pk)

        else:
            return Http404('INVALID FORM DETAILS')
    else:
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form' : form,'post' : current_post})

@login_required
def approve_comments(request,pk): # this pk is the primary key of comment not a blogpost
    comment = get_object_or_404(Comment,pk = pk)
    comment.approve()
    return redirect('blog:blog_details',pk = comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk = pk)
    post_pk = comment.post.pk # storing this because we are deleting this comment 
    comment.delete()
    return redirect('blog:blog_details',pk = post_pk)


    



    
    


