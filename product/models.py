from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    PROName = models.CharField(_("اسم المنتج :"), max_length=50)
    PRODesc = models.TextField(_("الوصف : "))
    PROImage = models.ImageField( upload_to='productImg' , verbose_name=_("Image "))
    PROCreated = models.DateTimeField(verbose_name=_("Create At "), default=timezone.now)
    PROSlug = models.SlugField(verbose_name= _("Product Slug"), blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.PROName

    def save(self, *args, **kwargs):
        if not self.PROSlug:
            self.PROSlug = slugify(self.PROName)
        super(Product, self).save(*args, **kwargs)