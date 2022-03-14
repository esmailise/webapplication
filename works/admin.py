from django.contrib import admin

# Register your models here.
from .models import works,Category,Gallery


admin.site.register(works)
admin.site.register(Category)
admin.site.register(Gallery)


