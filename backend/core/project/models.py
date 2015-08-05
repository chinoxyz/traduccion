
from django.db import models
from django.db.models.fields import CharField, FloatField, DateTimeField, \
    TextField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField,\
    OneToOneField

from backend.core.language.models import Language
from backend.core.user.models import AppUser


class Project(models.Model):
    owner = ForeignKey(AppUser)
    title = CharField(max_length=120)
    estimated_price = FloatField(null=True, blank=True)
    
    status = IntegerField(default = 0)
    creation_date = DateTimeField(auto_now_add=True)
    modification_date = DateTimeField(auto_now=True)
    
    details = TextField()
    conditions = TextField()
    information = TextField()
    expected_deadline = DateTimeField()
    
    specifications = TextField(blank=True)
    adaptations = TextField(blank=True)



class TraductionProject(Project):
    text = TextField(null=True, blank=True)
    textURL = CharField(max_length = 256, null=True, blank=True)
    origin_language = ForeignKey(Language, related_name="origin")
    destination_language = ForeignKey(Language, related_name="destiny")
    
    number_of_words = IntegerField(null=True, blank=True)
    number_of_pages = IntegerField(null=True, blank=True)
    
class ProjectAsignation(models.Model):
    project = ForeignKey(Project)
    worker = ForeignKey(AppUser)
    worker_price = FloatField(null=True, blank=True)
    creation_date = DateTimeField(auto_now_add=True)
    finish_date = DateTimeField(null=True, blank=True)
    deadline = DateTimeField()    
    