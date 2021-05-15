from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
  # 모델로부터 객체 목록을 전달 받도록 한다. (.object)
  blogs = Blog.objects   # 쿼리셋 # 메소드
  return render(request, 'home.html', {'blogs' : blogs})

  #쿼리셋과 메소드의 형식
  # 모델.쿼리셋(objects).메소드
  # 메소드 : all, count, first, last 등등

def detail(request, blog_id):
  # blog_detail = blog_id번째의 블로그 객체
  blog_detail = get_object_or_404(Blog, pk = blog_id)

  return render(request, 'detail.html', {'blog' : blog_detail})

#new.html을 띄워주는 함수
def new(request):
  return render(request, 'new.html')

#입력받은 내용을 데이터베이스에 넣어준다
def create(request):
  blog = Blog()
  blog.title = request.GET['title']
  blog.body = request.GET['body']
  blog.pub_date = timezone.datetime.now()
  blog.save() #데이터베이스에 저장하는 쿼리셋 메소드
  return redirect('/blog/'+str(blog.id)) #url은 항상 str, blog.id는 int ->  형변환 필요
