from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name=_("* نام تگ"), max_length=50)
    slug = models.SlugField(verbose_name=_("* اسلاگ"))

    class Meta:
        verbose_name = _("تگ")
        verbose_name_plural = _("تگ ها")

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(verbose_name=_("* نام تگ"), max_length=50)
    slug = models.SlugField(verbose_name=_("* اسلاگ"))

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

    def __str__(self):
        return self.name    

class Article(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name=_("* نویسنده"), on_delete=models.DO_NOTHING)
    id_post = models.UUIDField(verbose_name=_("آیدی پست"), unique=True, auto_created=True, help_text="دست نزن مَردَک")
    title = models.CharField(verbose_name=_("* عنوان"), max_length=50)
    content = RichTextField(verbose_name="* محتوا")
    image = models.ImageField(verbose_name=_("* تصویر"), upload_to=f"images/posts/{title}/")
    download_help = RichTextField(verbose_name="راهنمای دانلود", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("* دسته بندی"), on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, verbose_name=_("* تگ ها"))
    date_created = models.DateTimeField(verbose_name=_("* تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    view_visit = models.IntegerField(verbose_name=_("تعداد بازدید"), default=0, editable=False)

    
    
    class Meta:
        verbose_name = _("مقاله* ")
        verbose_name_plural = _("* مقاله ها")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk, 'title': self.title})

class Gallery(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("* مقاله"), on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name=_("* عنوان"), max_length=50)
    image = models.ImageField(verbose_name=_("* تصویر"), upload_to=f"images/galleries/{article}/")

    class Meta:
        verbose_name = _("عکس")
        verbose_name_plural = _("گالری")

    def __str__(self):
        return self.title

class Downloadbox(models.Model):
    title = models.CharField(verbose_name=_("* عنوان"), max_length=50)
    url = models.URLField(verbose_name=_("* لینک دانلود فایل"), max_length=200)
    

    class Meta:
        verbose_name = _("فایل")
        verbose_name_plural = _("باکس دانلود")

    def __str__(self):
        return self.title
 
class Comment(models.Model):
    name = models.CharField(verbose_name=_("* نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(verbose_name=_("* ایمیل"), max_length=254)
    text = models.TextField(verbose_name=_("* متن نظر"))
    date_send = models.DateTimeField(verbose_name=_("* تاریخ ارسال"), auto_now=False, auto_now_add=False)
    status = models.BooleanField(verbose_name=_("تایید شده"))
    
    
    class Meta:
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")

    def __str__(self):
        return self.name