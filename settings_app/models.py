from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
# Create your models here.

class Setting(models.Model):
    site_title = models.CharField(verbose_name=_("عنوان سایت"), max_length=50)
    site_logo = models.ImageField(verbose_name=_("لوگوی سایت"), upload_to="images/logos/")
    site_url = models.URLField(verbose_name=_("آدرس سایت"), max_length=200, help_text=_("https://meytisgame.ir"))
    site_copyright = models.CharField(verbose_name=_("قانون کپی رایت"), max_length=50)
    site_creator = models.CharField(verbose_name=_("نام صاحب سایت"), max_length=50)
    site_description = models.TextField(verbose_name=_("توضیحات سایت"))
    site_keywords = models.TextField(verbose_name=_("کلمات کلیدی سایت"))

    class Meta:
        verbose_name = _("تنظیم")
        verbose_name_plural = _("تنظیمات")
        
    def __str__(self):
        return self.site_title

class SocialNetwork(models.Model):
    """
        use admin.tabularinline
    """
    setting = models.ForeignKey(Setting, verbose_name=_("تنظیم"), on_delete=models.DO_NOTHING, related_name="socials")
    name = models.CharField(verbose_name=_("نام شبکه اجتماعی"), max_length=50, help_text=_("e.g: instagram"))
    url = models.URLField(verbose_name=_("لینک"), max_length=200, help_text=_("e.g: https://instagram.com/username/"))

    class Meta:
        verbose_name = _("شبکه اجتماعی")
        verbose_name_plural = _("شبکه های اجتماعی")

    def __str__(self):
        return self.name


class Ads(models.Model):
    text = RichTextField(verbose_name=_("توضیحات"))
    
    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات")
    
    def __str__(self):
        return 'توضیحات تبلیغ'

class Contact(models.Model):
    name = models.CharField(verbose_name=_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(verbose_name=_("ایمیل"), max_length=254)
    subject = models.CharField(verbose_name=_("عنوان تماس"), max_length=50)
    text = models.TextField(verbose_name=_("متن نظر"))
    date_sent = models.DateTimeField(verbose_name=_("تاریخ ارسال"), auto_now=False, auto_now_add=False)    
    accept = models.BooleanField(verbose_name=_("خواندن"), default=False)
    
    class Meta:
        verbose_name = _("تماس")
        verbose_name_plural = _("تماس های کاربران")
        ordering = ['-date_sent']
    
    def __str__(self):
        return self.name