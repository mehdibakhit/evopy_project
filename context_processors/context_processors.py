from blog_app.models import Article,Category

def my_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}