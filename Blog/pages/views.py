from django.shortcuts import render
from authors.models import Author
from Articles.models import Article
# Create your views here.


def home(request):
    articles = Article.objects.order_by('date').all()
    authors = Author.objects.all()[0:3]
    context = {
        'articles' : articles,
        'authors' : authors
    }
    return render(request, 'index.html', context)