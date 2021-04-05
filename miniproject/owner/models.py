from django.db import models

# Create your models here
class User(models.Model):
    CATEGORY = (
        ('Owner', 'Owner'),
        ('Staff', 'Staff'),
        ('Member', 'Member')
    )
    Name = models.CharField(max_length=64, null=True)
    Email = models.EmailField(max_length=64, null=True)
    Mobile= models.IntegerField()
    Roll = models.CharField(max_length=20, null=True)
    Username=models.CharField(max_length=64, null=True)   



   
class Menu(models.Model):
    CATEGORY=(
        ('Beverages','Beverages'),
        ('Thali','Thali'),
        ('snaks', 'snacks')
    )
    Menu_id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=50, null=True)
    Price= models.IntegerField(default=1, null=True)
    category= models.CharField(max_length=50, null=True, choices=CATEGORY)

class Transaction(models.Model):
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    date_added=models.DateTimeField(auto_now_add=True,null=True)
    Quantity=models.IntegerField(default=1)

class Payment(models.Model):
    CATEGORY = (
        ('Advance', 'Advance'),
        ('Due', 'Due')
    )
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Amount_paid = models.IntegerField(default=1, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

