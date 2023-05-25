from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Tool(models.Model):
    title = models.CharField(verbose_name=_("عنوان"), max_length=50)
    icon = models.ImageField(verbose_name=_("آیکن"), upload_to="images/icons/")
    version = models.CharField(verbose_name=_("ورژن"), max_length=50)
    url = models.URLField(verbose_name=_("لینک دانلود"), max_length=200)
    source = models.URLField(verbose_name=_("منبع"), max_length=200, help_text=_("آدرس سایت"))
    
    class Meta:
        verbose_name=_("ابزار")
        verbose_name_plural=_("ابزارها")
    
    def __str__(self):
        return self.title