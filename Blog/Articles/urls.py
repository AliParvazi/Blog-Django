from django.urls import path
from .views import index, article 

urlpatterns = [
    path('', index, name='articles'),
    path('<int:article_id>' , article, name='article')
]