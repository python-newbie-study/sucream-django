from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts
#         }
#     )

# vue 학습을 위해 추가
def vue_test(request):
    return render(request, 'blog/test.html')

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )

def login(request):
    print(request.method)
    if request.method == "POST":
         # create a form instance and populate it with data from the request:
        id = request.POST.get("loginId", None)
        pw = request.POST.get("loginPw", None)

        print(id)
        print(pw)

        if id == 'sucream' and pw == '1234':
            print("오리오리")
        else:
            print("삐빅")
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
        # return redirect('/blog#login')

    else:
        form = PostForm() #forms.py의 PostForm 클래스의 인스턴스
        return render(request, 'lotto/form.html', {'form' : form})  # 템플릿 파일 경로 지정, 데이터 전달
