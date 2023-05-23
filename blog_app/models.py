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
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk, 'title': self.title})
    def short_url(self):
        return reverse("article_detail_2", kwargs={"id_post": self.id_post})

class Gallery(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING, related_name='galleries')
    title = models.CharField(verbose_name=_("عنوان"), max_length=50)
    image = models.ImageField(verbose_name=_("تصویر"), upload_to=f"images/galleries/")

    class Meta:
        verbose_name = _("عکس")
        verbose_name_plural = _("گالری")

    def __str__(self):
        return self.title

class Downloadbox(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING, related_name='download_boxs')
    title = models.CharField(verbose_name=_("عنوان"), max_length=50)
    url = models.URLField(verbose_name=_("لینک دانلود فایل"), max_length=200)
    

    class Meta:
        verbose_name = _("فایل")
        verbose_name_plural = _("باکس دانلود")

    def __str__(self):
        return self.title
 
class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING, related_name="article_commnets")
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
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING ,related_name="seo")
    creator = models.ForeignKey(get_user_model(), verbose_name=_("SEO نویسنده"), on_delete=models.DO_NOTHING)
    description = models.CharField(verbose_name=_("Description"), max_length=165, help_text=_("max length: 165 character"))
    keywords = models.TextField(verbose_name=_("Keywords"), help_text=_("با کاما (,) از هم جدا کنید"))
    redirect = models.URLField(verbose_name=_("Redirect"), max_length=200, blank=True, null=True, default=None, help_text=_("میتواند خالی بماند"))
    refresh = models.CharField(verbose_name=_("Refresh"), max_length=100, blank=True, null=True, default=None, help_text=_("e.g: 3;url=https://www.mozilla.org --> میتواند خالی بماند"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    date_updated = models.DateTimeField(verbose_name=_("تاریخ آپدیت"), auto_now=True)
    
    
    class Meta:
        verbose_name = _("SEO")
        verbose_name_plural = _("SEOs")

    def __str__(self):
        return self.article.title

    def creator_name(self):
        return self.creator.username