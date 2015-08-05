# Create your models here.



from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField, ForeignKey
from django.db.models.fields import CharField,EmailField, BooleanField


#class tokenPassword(models.Model):
#    user = OneToOneField(User)
#    token = CharField()

class AppUser(models.Model):
    user = OneToOneField(User)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    initial_email = EmailField()
    email = EmailField()
    def change_password(self, password, newpassword):
        if self.user.check_password(password):
            self.user.set_password(newpassword)
            self.user.save()
            return True
        else:
            return False