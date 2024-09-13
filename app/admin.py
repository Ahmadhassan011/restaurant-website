from django.contrib import admin
from .models import home_images, Appetizers, Main_course, Dessert, Chef, Message
from django.contrib import messages

# Register your models here.

admin.site.register(home_images)
admin.site.register(Appetizers)
admin.site.register(Main_course)
admin.site.register(Dessert)
admin.site.register(Chef)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')


admin.site.site_header  =  "Flavorscape Bistro Admin"  
admin.site.site_title  =  "Flavorscape Bistro"
admin.site.index_title  =  "Flavorscape Bistro"