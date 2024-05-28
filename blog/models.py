from django.db import models
from django.utils import timezone
from shared.utils import jalali_converter

# My managers
class ArticleManager(models.Manager):
    def get_published_articles(self):
        return self.filter(status='p')

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('position',)
        
        

class Article(models.Model):
    STATUS_CHOICE = (
        ('d', 'پیش‌ نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
    description = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی اطلاعات')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name='وضعیت انتشار')
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_jalali_publish(self):
        return jalali_converter(self.publish)
    get_jalali_publish.short_description = 'زمان انتشار'
    
    def get_published_category(self):
        return self.category.filter(status=True)
    
    objects = ArticleManager()