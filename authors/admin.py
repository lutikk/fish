from django.contrib import admin
from authors.models import Mamonts

# Register your models here.



@admin.register(Mamonts)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "login", "password", 'first_name', 'last_name')



