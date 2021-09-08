
from django.shortcuts import get_object_or_404,render
from django.views.generic import ListView,DetailView,TemplateView
from .models import Post,Category,Tag
from .filter import PostFilter
from .forms import CommentForm
class post_view(ListView): 
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 5
    queryset = Post.objects.published()
    context_object_name = 'blog_list'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context
class post_detail(DetailView):
    template_name = 'blog/post.html'
    model = Post
    context_object_name = 'post_detail'
    pk_url_kwarg ='slug'
   
    
    def get_object(self):
        post = get_object_or_404(Post, slug = self.kwargs['slug'])
        ip_address = self.request.user.ip_address
        if ip_address not in post.hits.all():
            post.hits.add(ip_address)
        return post
class success(TemplateView):
    template_name = 'success.html'

class CategoryList(ListView):
    paginate_by = 5
    template_name = 'blog/categoryList.html'
    context_object_name = 'blog_list'
    model = Post
    def get_queryset(self):
        self.category = get_object_or_404(Category,slug = self.kwargs['slug'])
        post = Post.objects.filter(category = self.category)
        return post
    def get_context_data(self, **kwargs):
        context = super(CategoryList,self).get_context_data(**kwargs)
        context["category"] = self.category
       
        return context
class SearchList(ListView):
    models = Post
    paginate_by = 5
    template_name = 'blog/blog.html'
    context_object_name = 'blog_list'
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query :
            object_list = self.models.objects.filter(title__icontains=query)
        else:
            object_list = ""
        return object_list
    

class TagList(ListView):
    paginate_by = 5
    template_name = 'blog/taglist.html'
    context_object_name = 'tag_list'
    model = Post
    def get_queryset(self):
        self.tag = get_object_or_404(Tag,slug = self.kwargs['slug'])
        post = Post.objects.filter(tag = self.tag)
        return post
    def get_context_data(self, **kwargs):
        context = super(TagList,self).get_context_data(**kwargs)
        context["tag"] = self.tag
       
        return context
