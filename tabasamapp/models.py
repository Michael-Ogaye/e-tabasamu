from django.db import models


from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    name = models.CharField(max_length=80, blank=True)
    account_ref= models.TextField(max_length=254, blank=True)
    account_picture = CloudinaryField('images')

    
    

    def __str__(self):
        return f'{self.user.username} account'

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        if created:
            UserAccount.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        instance.account.save()