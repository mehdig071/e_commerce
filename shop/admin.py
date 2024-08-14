from django.contrib import admin
from shop.models.Slider import Slider
from django.utils.html import format_html
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.Image import Image
from shop.models.Setting import Setting
from shop.models.Social import Social
from shop.models.Page import Page
from django.db import models
from ckeditor.widgets import CKEditorWidget
from shop.models.Navcollection import Navcollection
from shop.models.Carrier import Carrier
from shop.models.OrderDetail import OrderDetail
from shop.models.Order import Order
from shop.models.Method import Method

class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'link')
    list_display_links = ('name',)
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_head', 'is_foot', 'is_checkout')
    list_display_links = ('name',)
    list_editable = ('is_head', 'is_foot', 'is_checkout')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    exclude = ('slug',)
    
    
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'display_logo', 'street', 'city')
    list_display_links = ('name',)
    
    def display_logo(self, obj):
        return format_html(f'<img src="{ obj.logo.url }" width="20" />')
    
    display_logo.short_description = 'logo'
    
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'
    
class NavcollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'

   
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','price', 'display_image')
    list_display_links = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" height="50" width="60" />')
    
    display_image.short_description = 'image'
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mega', 'display_image')
    list_display_links = ('name',)
    list_editable = ('is_mega',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" height="50" width="60" />')
    
    display_image.short_description = 'image'
    exclude = ('slug',)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name', 'solde_price', 'is_best_seller','is_featured', 'is_special_offer', 'is_new_arrival', 'regular_price', 'display_image')
    list_display_links = ('name',)
    list_editable = ('is_best_seller','is_featured', 'is_special_offer', 'is_new_arrival')
    list_per_page = 5
    list_filter = ('created_at','updated_at')
    search_fields = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    
    def display_image(self, obj):
        first_image = obj.images.first()
        if not first_image:
            return ''
        return format_html(f'<img src="{ first_image.image.url }" height="90" width="80" />')
    
    exclude = ('slug',)
    display_image.short_description = 'image'
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'billing_address', 'shipping_address', 'quantity', 'taxe', 'order_cost',
                    'order_cost_ttc', 'status', 'is_paid', 'carrier_name', 'carrier_price', )
    list_display_links = ('client_name',)
    list_editable = ('status',)
    list_filter = ('is_paid', 'created_at', 'updated_at')
    search_fields = ('client_name', 'billing_address', 'shipping_address', 'carrier_name', 'payment_method')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity', 'solde_price', 'sub_total_ht', 'sub_total_ttc')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('product_name', 'quantity', 'solde_price', 'sub_total_ht', 'sub_total_ttc')

class MethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','display_image', 'is_available')
    list_display_links = ('name',)
    list_filter = ('is_available', 'created_at', 'updated_at')
    search_fields = ('name', 'description',)
    
    def display_image(self, obj):
        first_image = obj.logo
        if not first_image:
            return ''
        return format_html(f'<img src="{ first_image.url }" height="40" width="100" />')
    
    display_image.short_description = 'image'


admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Navcollection, NavcollectionAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Method, MethodAdmin)

