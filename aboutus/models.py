from typing import Text
from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class AboutUs(models.Model):
    Title = models.CharField(_("عنوان"), max_length=200)
    summary = models.TextField(_("خلاصه درباره ما"))
    content = RichTextField(_("محتوا درباره"))
    photo = models.ImageField(_("عکس"), upload_to='aboutus/',)
    links  = models.ManyToManyField("LinkAcount", verbose_name=_("رسانه ها"))
    created_at = models.DateTimeField(_("زمان انتشار"),default=timezone.now)

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'    

    def __str__(self):
        return self.Title

class LinkAcount(models.Model):
    choose =(
        ('fa fa-facebook', 'فیس بوک'),
        ('fa fa-twitter', 'توییتر'),
        ('fa fa-linkedin', 'لینک دین'),
        ('fa fa-google-plus', 'گوگل پلاس'),
        ('fa fa-instagram', 'اینستا گرام'),
        ('fa fa-whatsapp', 'واتس اپ'),     
    )
    name = models.CharField(_("نام رسانه"), max_length=50)
    Acounturl = models.URLField(_("ادرس رسانه"), max_length=200)
    icons = models.CharField(_("انتخاب شمایل"), choices=choose,max_length=200)

    class Meta:
        verbose_name = 'رسانه  اجتماعی'
        verbose_name_plural = 'رسانه های اجتماعی'    

    def __str__(self):
        return self.name