from django.contrib import admin
from .models import Facility,AccountStatement,Transaction,UserAccount

# Register your models here.
admin.site.register(Facility)
admin.site.register(Transaction)
admin.site.register(AccountStatement)
admin.site.register(UserAccount)
