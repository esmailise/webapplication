from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class works (models.Model):
    description = models.CharField(_("توضیحات"),max_length=100)
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField(_("قیمت انجام شده"))
    pub_date = models.DateField(auto_now=False,auto_now_add=True)
    photo  = models.ImageField(_("عکس"), upload_to='works/')
    category = models.ForeignKey("Category", on_delete = models.CASCADE,)

    class Meta:
        verbose_name = 'کار'
        verbose_name_plural = 'کار ها'  

    def __str__(self):
        return self.category.name_work_fa


class Category (models.Model):
    name_work_fa = models.CharField(_("نام کار فارسی"), max_length=50)
    name_work_en = models.CharField(_("نام کار انگلیسی"), max_length=50)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها' 

    def __str__(self):
        return self.name_work_fa
    


class Gallery (models.Model):
    photo = models.ImageField(_("عکس"), upload_to='gallery/')
    
    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'
    

    
        
    

    
    
    

    