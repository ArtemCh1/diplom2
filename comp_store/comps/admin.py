from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProductStatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    form = ProductAdminForm
    list_display = ('name','created_at', 'views', 'category', 'status', 'seller')
    list_filter = ('category', 'status', 'seller')
    search_fields = ('name',)
    ordering = ('-created_at',)
    list_display_link = ('name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductStatus, ProductStatusAdmin)
admin.site.register(Product, ProductAdmin)