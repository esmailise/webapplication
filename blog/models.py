from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("عنوان"),max_length = 150)
    description = models.CharField(_("توضیحات"),max_length = 150)
    content = RichTextField()
    created_at = models.DateTimeField(_("زمان انتشار"),default=timezone.now)
    author = models.ForeignKey(User,verbose_name=_("نویسنده"),on_delete = models.CASCADE)
    image = models.ImageField(_("تصویر"),upload_to="blogs/",)
    category = models.ForeignKey("Category", on_delete=models.CASCADE,verbose_name=_("دسته بندی"),related_name="blog")
    tags = models.ManyToManyField("Tag",verbose_name=_("تگ ها"),related_name = "blogs")

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_("عنوان"),max_length = 150)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'    

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    update_at = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها' 

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(_("نام کاربر"), max_length=50)
    email = models.EmailField(_("ادرس الکترونیکی"),max_length=254)
    message = models.TextField(_("متن مورد نظر"))
    data = models.DateField(_("تاریخ انتشار"),auto_now= False,auto_now_add = True)
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE,verbose_name=_("مقاله"),related_name="comments")

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها' 

    def __str__(self):
        return self.email
    

    