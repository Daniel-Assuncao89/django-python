from django.views import generic

from blog.models import Post


# toda vez q bater na url home, vai executar a queryset e renderizar no index.html
class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
