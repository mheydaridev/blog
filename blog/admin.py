from django.contrib import admin
from .models import Article, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_jalali_publish', 'status', 'get_categories')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ( '-status', '-publish')

    def get_categories(self, obj):
        return '، '.join([category.title for category in obj.get_published_category()])
    get_categories.short_description = 'دسته بندی ها'


admin.site.register(Article, ArticleAdmin)