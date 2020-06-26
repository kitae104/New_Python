from django.shortcuts import render
from tutorial.community.forms import *


def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html',{'form':form})

def list(request):
    articleList = Article.objects.all();           # 모든 컬럼 가져오기
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})
