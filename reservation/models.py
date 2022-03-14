from django.db import models
from django.utils import translation
from django.utils.translation import gettext as _
from works.models import Category
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class reservation(models.Model):
    statuses =(
        (False,'انجام نشده'),
        (True,'انجام شده')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="نام کاربر",null=True)
    email = models.EmailField(_("ایمیل"), max_length=245,null=True)
    phone = models.CharField(_("تلفن"),max_length=20,null=False)
    data = models.DateField(_("تاریخ"),default=timezone.now,null=False)
    time = models.TimeField(_("ساعت"), default=timezone.now,null=False)
    address = models.CharField(_("آدرس"), max_length=250,null=False)
    categorys = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='نوع کار')
    status = models.BooleanField(_('وضعیت کار'),choices=statuses,default=False,null=True)

    class Meta : 
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو ها'

    def __str__(self):
        return self.email
    



