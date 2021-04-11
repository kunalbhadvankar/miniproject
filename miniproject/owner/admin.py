from .models import user, Payment ,Menu,Transaction

from django.contrib import admin
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
   
    list_display=("Menu_id","Name","Price", "category")



class TransactionAdmin(admin.ModelAdmin):
    list_display=("Member_id","Menu_id","Quantity")



admin.site.register(user)
admin.site.register(Payment)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Transaction,TransactionAdmin)

