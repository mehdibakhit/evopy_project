from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True, unique=True, allow_unicode=True,verbose_name="اسلاگ")
    image = models.ImageField(upload_to='images/articles',verbose_name="تصویر")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    # content = RichTextField(blank=True,null=True)  # اینجا محتوای HTML غنی ذخیره میشه
    body = HTMLField(blank=True,null=True)
    category = models.ManyToManyField(Category,related_name="articles")
    image = models.ImageField(upload_to='images/articles',verbose_name="تصویر")
    slug = models.SlugField(blank=True, null=True, unique=True, allow_unicode=True,verbose_name="اسلاگ")
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, verbose_name="بروزرسانی")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"



    def get_absolute_url(self):
        return reverse("blog_app:article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # ساخت اسلاگ با پشتیبانی از فارسی (تبدیل فاصله به خط تیره)
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class Message(models.Model):
    name = models.CharField(max_length=15,null=True,blank=True)
    last_name = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    message = models.TextField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.name

