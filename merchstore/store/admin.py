from django.contrib import admin
from .models import Product, Category, Customer,Size, Cart, CartItem
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'image', 'category', 'sizes']
    list_display = ('get_sizes',)

    def get_sizes(self, obj):
        return "\n".join([p.sizes for p in obj.size.all()])
    
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    
class CartInline(admin.StackedInline):
    model = Cart
    can_delete = False
    inlines = [CartItemInline]  

class CartItemAdmin(admin.ModelAdmin):
    model: CartItem
    list_display = ('product', 'quantity', 'date_added')

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CartInline]
    def cart_items(self, obj):
        cart = obj.cart
        cart_items = cart.cartitem_set.all()
        for  item in cart_items:
            print('item ',item)
        return ", ".join([str(item) for item in cart_items])
    cart_items.short_description = "Cart Items"
    
    list_display = ('user', 'shipping_address', 'billing_address')



class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

    list_display = ('customer', 'cart_items')

    def cart_items(self, obj):
        cart_items = obj.cartitem_set.all()
        return ", ".join([str(item) for item in cart_items])

    cart_items.short_description = "Cart Items"

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)