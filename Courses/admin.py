from django.contrib import admin
from .models import Day, Career, Course, Time, Button
from django.urls import reverse
from django.utils.html import format_html

class MyModelAdmin(admin.ModelAdmin):
    
  def my_custom_button(self, obj):
    return format_html('<a class="button" href="{}">Ejecutar código específico</a>',reverse('createTables'))
  
  my_custom_button.short_description = 'Ejecutar código específico'
  list_display = ('my_custom_button',)
    
# Register your models here.
admin.site.register(Day)
admin.site.register(Career)
admin.site.register(Course)
admin.site.register(Time)
admin.site.register(Button, MyModelAdmin)
