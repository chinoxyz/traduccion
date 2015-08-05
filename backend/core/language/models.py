
from django.db import models
from django.db.models.fields import CharField, FloatField, DateTimeField,\
    TextField, IntegerField
from django.db.models.fields.related import ForeignKey


from backend.core.user.models import AppUser





class Language(models.Model):
    code = CharField(max_length=5)
    name = CharField(max_length=50)

