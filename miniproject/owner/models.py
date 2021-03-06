from django.db import models
from django.contrib.auth.models import User

# Create your models here
class user(models.Model):
    user = models.OneToOneField(User,default=None, null=True, on_delete=models.CASCADE)

    Name = models.CharField(max_length=50, null=True)


   
    Mobile= models.IntegerField()
    department = models.CharField(max_length=50, null=True)
    Pay_mode = models.CharField(max_length=50, null=True)
    Time_mode = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username
    
 
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
    Member_id = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    Menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    date_added=models.DateTimeField(auto_now_add=True,null=True)
    Quantity=models.IntegerField(default=1)
    Paid = models.BooleanField(default=0)


class Payment(models.Model):
    CATEGORY = (
        ('Advance', 'Advance'),
        ('Due', 'Due')
    )
    Member_id = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    Amount_paid = models.IntegerField(default=1, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    Pay_category = models.CharField(max_length=50, null=True, choices=CATEGORY)

