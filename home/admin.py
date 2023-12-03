from django.contrib import admin

from home.models import Car, Mark , Color

# Register your models here.

   

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
   list_display = ['name']




@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
   list_display = ['mark', 'model', 'price','color']
   list_filter = ['mark']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
   list_display = ['color']
