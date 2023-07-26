from django.contrib import admin
from shop.models import cards,Category,Product
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(cards)
admin.site.register(Category,Categoryadmin)
class Productadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','created','updated']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,Productadmin)


