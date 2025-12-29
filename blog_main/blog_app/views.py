from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from  django.http import HttpResponse
from .models import Category, Blog
from django.shortcuts import get_object_or_404
def home(request):
    categories = Category.objects.all()
    feature_posts= Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at')
    posts = Blog.objects.filter(status="Published").order_by("-created_at")
    print(posts)
    context = {'categories': categories, 'feature_posts': feature_posts, 'posts': posts}
    return render(request, 'home.html', context)

def post_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status="Published").order_by("-created_at")
    #if u want to do consum action of error handling then use try and except block
    # try:
    #     category = Category.objects.get(id=category_id)
    # except :
    #     return redirect('home')  # Redirect to home if category doesn't exist
    category = get_object_or_404(Category, id=category_id)  # this is good way to handling error or page not found 
    return render(request, 'category_posts.html', {'posts': posts, 'category': category}) # 