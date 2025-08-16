from django.contrib import admin

# Register your models here.
from .models import Category, Banner, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_popular')
    list_editable = ('is_popular',)
    search_fields = ('name',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'is_top_deal')
    list_editable = ('is_top_deal',)
    search_fields = ('name',)
    list_filter = ('category',)
