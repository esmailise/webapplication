from django.contrib import admin
from .models import Blog,Category,Tag,Comment
# Register your models here.
#admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','author')
    list_filter = ('category',)
    search_fields = ('title',)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Blog,BlogAdmin)