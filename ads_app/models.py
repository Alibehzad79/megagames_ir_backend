from django.db import models
from django.utils.translation import gettext_lazy as _
from blog_app.models import Article, Tag, Category
# Create your models here.

class ArticleDetailPageAds(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING, related_name="ads")
    client = models.CharField(verbose_name=_("سفارش دهنده"), max_length=50)
    image = models.ImageField(verbose_name=_("عکس / گیف"), upload_to="ads/images/")
    url = models.URLField(verbose_name=_("لینک ارجاع"), max_length=200)
    date_start = models.DateField(verbose_name=_("تاریخ شروع"), auto_now=False, auto_now_add=False)
    date_end = models.DateField(verbose_name=_("تاریخ پایان"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(verbose_name=_("فعال / غیرفعال"), default=True)
    

    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات صفحه ی مقاله")

    def __str__(self):
        return self.client

class HomePageAds(models.Model):
    client = models.CharField(verbose_name=_("سفارش دهنده"), max_length=50)
    image = models.ImageField(verbose_name=_("عکس / گیف"), upload_to="ads/images/")
    url = models.URLField(verbose_name=_("لینک ارجاع"), max_length=200)
    date_start = models.DateField(verbose_name=_("تاریخ شروع"), auto_now=False, auto_now_add=False)
    date_end = models.DateField(verbose_name=_("تاریخ پایان"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(verbose_name=_("فعال / غیرفعال"), default=True)
    

    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات صفحه خانه")

    def __str__(self):
        return self.client


class TagPageAds(models.Model):
    tag = models.ForeignKey(Tag, verbose_name=_("تگ"), on_delete=models.DO_NOTHING, related_name='ads')
    client = models.CharField(verbose_name=_("سفارش دهنده"), max_length=50)
    image = models.ImageField(verbose_name=_("عکس / گیف"), upload_to="ads/images/")
    url = models.URLField(verbose_name=_("لینک ارجاع"), max_length=200)
    date_start = models.DateField(verbose_name=_("تاریخ شروع"), auto_now=False, auto_now_add=False)
    date_end = models.DateField(verbose_name=_("تاریخ پایان"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(verbose_name=_("فعال / غیرفعال"), default=True)
    

    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات صفحه تگ ها")

    def __str__(self):
        return self.client

class CategoryPageAds(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("تگ"), on_delete=models.DO_NOTHING, related_name='ads')
    client = models.CharField(verbose_name=_("سفارش دهنده"), max_length=50)
    image = models.ImageField(verbose_name=_("عکس / گیف"), upload_to="ads/images/")
    url = models.URLField(verbose_name=_("لینک ارجاع"), max_length=200)
    date_start = models.DateField(verbose_name=_("تاریخ شروع"), auto_now=False, auto_now_add=False)
    date_end = models.DateField(verbose_name=_("تاریخ پایان"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(verbose_name=_("فعال / غیرفعال"), default=True)
    

    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات صفحه دسته بندی ها")

    def __str__(self):
        return self.client    


class SearchPageAds(models.Model):
    client = models.CharField(verbose_name=_("سفارش دهنده"), max_length=50)
    image = models.ImageField(verbose_name=_("عکس / گیف"), upload_to="ads/images/")
    url = models.URLField(verbose_name=_("لینک ارجاع"), max_length=200)
    date_start = models.DateField(verbose_name=_("تاریخ شروع"), auto_now=False, auto_now_add=False)
    date_end = models.DateField(verbose_name=_("تاریخ پایان"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(verbose_name=_("فعال / غیرفعال"), default=True)
    

    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات صفحه جستوجو")

    def __str__(self):
        return self.client