from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

# posts = [
#     {
#         "author" : "UserTest1",
#         "title": "BLog Post 1",
#         "Content": "First post on the Blog",
#         "date_posted":"15/2/2020"
#     },
#     {
#         "author" : "UserTest2",
#         "title": "BLog Post 2",
#         "Content": "Second post on the Blog",
#         "date_posted":"15/2/2020"
#     }
# ]

def home(request):
    content ={ "posts" : Post.objects.all() }
    # return HttpResponse("<h1>Hello Django</h1>")
    return render(request,"blog/home.html", content )

def about(request):
    # return HttpResponse("<h1>This is a django Blog App!!!</h1>")
    return render(request, "blog/about.html",{"title": "About"})