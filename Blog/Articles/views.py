from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from Articles.models import Article
from authors.models import Author
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-title')
    
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)    

    context = {
        'articles' : paged_articles
    }
    return render(request, 'articles/index.html', context)

def article(request, article_id):
    article = get_object_or_404(Article ,pk=article_id)
    author  = Author.objects.filter(article__author = article.author)[0]
    context = {
        'article' : article,
        'author' : author
    }
    return render(request, 'articles/article.html', context) 