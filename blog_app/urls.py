from django.urls import path
from blog_app import views


app_name = "blog_app"

urlpatterns = [
    path('detail/<str:slug>/', views.article_detail, name='article_detail'),
    path('list/', views.article_list, name='article_list'),
    path('category/<slug:slug>', views.category_list, name='category_list'),
    path('contactUs', views.contactus, name='contact_us'),
]

