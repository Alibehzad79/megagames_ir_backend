from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class SaerchResault(models.Model):
    query_name = models.CharField(verbose_name=_("نام کلید واژه"), max_length=50)
    research_count = models.IntegerField(verbose_name=_("تعداد دفعات سرچ"), default=0)
    
    class Meta:
        verbose_name = _("جستوجو")
        verbose_name_plural = _("نتیجه جستوجو")
        
    def __str__(self):
        return self.query_name
        