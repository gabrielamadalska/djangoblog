from django.shortcuts import render
from django.utils import timezone
from .models import Post

#kropka ocznacza bieżący katalog/aplikacje

#funkcja post_list ktora pobiera i zwraca wartość wowalaną dzieki innej
#funkcji - render, ktora zlozy w calosc szablon html
def post_list(request):
    posts = Post.objects.filter(publish_date__lte = timezone.now()).order_by('publish_date')

    return render(request, 'blog/post_list.html', {'posts' : posts})



