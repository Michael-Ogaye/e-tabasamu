from django.db import models
import random
import string

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Facility(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=300,blank=True, null=True)
    address=models.CharField(max_length=150,blank=True, null=True)
    tel_no=models.IntegerField(blank=True, null=True)
    email_f=models.EmailField(blank=True,null=True)


    def __str__(self):
        return f'{self.name} '

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    name = models.CharField(max_length=80, blank=True)
    facility=models.ManyToManyField(Facility,related_name='accounts')
    account_ref= models.TextField(max_length=254, blank=True)
    account_picture = CloudinaryField('images')
    creation_date=models.DateField(auto_now_add=True)
    phone_no=models.IntegerField(blank=True, null=True)

    

    
    

    def __str__(self):
        return f'{self.user.username} account'

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        if created:
            UserAccount.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        instance.account.save()

class AccountStatement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='statements')
    facility=models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='statements')
    
    def __str__(self):
        return f'{self.user.username} account statement'





class Transaction(models.Model):
    acctype=(

    ('withdrawal','widhdrawal'),
    ('deposit','deposit'),

    )
    


    type=models.CharField(choices=acctype, max_length=45)
    time_made=models.DateTimeField(auto_now_add=True)
    transaction_code=models.CharField(max_length=254)
    amount=models.FloatField()
    facility=models.ForeignKey(Facility,on_delete=models.CASCADE)
    maker=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='transactions')
    statement=models.ForeignKey(AccountStatement,on_delete=models.CASCADE,null=True)
    


    @property
    def code_gen(self):
       str_size=12
       allowed_chars = string.ascii_letters
       self.transaction_code= ''.join(random.choice(allowed_chars) for x in range(str_size))


    def __str__(self):
        return f'{self.type}'
       




