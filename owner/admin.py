from .models import User,History,Menu,Transaction

from django.contrib import admin
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display=("Menu_id","Name","Price")

class UserAdmin(admin.ModelAdmin):
    list_display= ("Name", "Email", "Mobile", "Roll", "Username",)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("Member_id","Menu_id","Quantity")



admin.site.register(User, UserAdmin)
admin.site.register(History)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Transaction,TransactionAdmin)
