from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Contactus(models.Model):
    name  = models.CharField(_("نام کاربر"), max_length=50)
    email = models.EmailField(_("ایمیل کاربر"), max_length=254)
    message = models.TextField(_("متن کاربر"))

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        
    def __str__(self):
        return self.email

