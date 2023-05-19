from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.crypto import get_random_string
# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name=_("نام تگ"), max_length=50, unique=True)
    slug = models.SlugField(verbose_name=_("اسلاگ"), unique=True)

    class Meta:
        verbose_name = _("تگ")
        verbose_name_plural = _("تگ ها")

    def __str__(self):
        return self.name + " | " + self.slug 
    
class Category(models.Model):
    name = models.CharField(verbose_name=_("نام دسته بندی"), max_length=50, unique=True)
    slug = models.SlugField(verbose_name=_("اسلاگ"), unique=True)

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

    def __str__(self):
        return self.name + " | " + self.slug   


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name=_("نویسنده"), on_delete=models.DO_NOTHING)
    id_post = models.CharField(verbose_name=_("آیدی پست"), default=get_random_string(7), max_length=7, unique=True, help_text="دست نزن مَردَک", blank=True, null=True)
    title = models.CharField(verbose_name=_("عنوان"), max_length=50)
    content = RichTextField(verbose_name="محتوا")
    image = models.ImageField(verbose_name=_("تصویر"), upload_to=f"images/posts/")
    download_help = RichTextField(verbose_name="راهنمای دانلود", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("دسته بندی"), on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, verbose_name=_("تگ ها"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    view_visit = models.IntegerField(verbose_name=_("تعداد بازدید"), default=0, editable=False)
    active = models.BooleanField(verbose_name=_("فعال"), default=False)
    
    
    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقاله ها")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk, 'title': self.title})

class Gallery(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name=_("عنوان"), max_length=50)
    image = models.ImageField(verbose_name=_("تصویر"), upload_to=f"images/galleries/{article}/")

    class Meta:
        verbose_name = _("عکس")
        verbose_name_plural = _("گالری")

    def __str__(self):
        return self.title

class Downloadbox(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name=_("عنوان"), max_length=50)
    url = models.URLField(verbose_name=_("لینک دانلود فایل"), max_length=200)
    

    class Meta:
        verbose_name = _("فایل")
        verbose_name_plural = _("باکس دانلود")

    def __str__(self):
        return self.title
 
class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name=_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(verbose_name=_("ایمیل"), max_length=254)
    text = models.TextField(verbose_name=_("متن نظر"))
    date_send = models.DateTimeField(verbose_name=_("تاریخ ارسال"), auto_now=False, auto_now_add=False)
    status = models.BooleanField(verbose_name=_("تایید شده"))
    
    
    class Meta:
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")

    def __str__(self):
        return self.name
    
class Seo(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = _("SEO")
        verbose_name_plural = _("SEOs")

    def __str__(self):
        return self.article.title
    # TODO SEO