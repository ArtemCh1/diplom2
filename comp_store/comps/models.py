from django.db import models

from oauth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class ProductStatus(models.Model):
    title = models.CharField(max_length=255, verbose_name='Статус')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Статус Продукта'
        verbose_name_plural = 'Статусы Продукта'
        ordering = ['title']


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photos/product/%Y/%m/%d/', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    status = models.ForeignKey(ProductStatus, on_delete=models.PROTECT, related_name='products', verbose_name='Статус')
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products', verbose_name='Продавец')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']
    