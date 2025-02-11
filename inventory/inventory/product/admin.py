from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Brand, Category, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display brand name in list
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):  # Use MPTTModelAdmin for hierarchical categories
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass