from django.shortcuts import render
from .models import Post

# Create your views here.
def price(request):
    posts = Post.objects
    return render(request, 'price/price.html', {'posts' : posts})