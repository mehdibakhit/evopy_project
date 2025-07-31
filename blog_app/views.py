from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from blog_app.models import Article, Category, Message
from .form import ContactUsForm,MessageForm


# Create your views here.
def article_detail(request, slug):  # پارامتر slug را اضافه کنید
    article = get_object_or_404(Article, slug=slug)  # فقط یک مقاله بر اساس slug
    return render(request, "blog_app/article_detail.html", {'article': article})


def article_list(request):
    articles = Article.objects.all().order_by("-created")
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "blog_app/article_list.html", {'articles': object_list})


def category_list(request, slug):
    articles = Article.objects.all().order_by("-created")
    categories = get_object_or_404(Category, slug=slug)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    articles = categories.articles.all()
    return render(request, "blog_app/category_list.html", {'articles': object_list, "categories": categories})


def contactus(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(data= request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            Message.objects.create(name=name, last_name=last_name, email=email, phone_number=phone_number,message=message)
    return render(request, "blog_app/contact_us.html", {'form': form})
