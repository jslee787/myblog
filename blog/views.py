from django.shortcuts import render, redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post

def index(request):
    #블로그 메인 페이지
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    #글 쓰기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  #가저장
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:index')   # 등록 후 블로그홈으로 이동
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)