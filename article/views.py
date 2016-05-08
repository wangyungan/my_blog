from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    return HttpResponse("Hello world django.")

def test(request):
    post = Article.objects.all();
    name = 'DEAMON'
    return render(request, 'test.html', locals())
