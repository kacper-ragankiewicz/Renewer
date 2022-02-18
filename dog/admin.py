from django.contrib import admin
from .models import Dog
# Register your models here.

class DogAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis', 'gotowe')

admin.site.register(Dog,DogAdmin)