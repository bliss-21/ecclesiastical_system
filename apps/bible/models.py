# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Testament(models.Model):
    
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testament'
        app_label = 'bible'

    def __str__(self):
        return self.name

class Book(models.Model):
    
    testament = models.ForeignKey('Testament', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'
        app_label = 'bible'

    def __str__(self):
        return self.name

class Verse(models.Model):
    
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    verse = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verse'
        app_label = 'bible'
        
    def __str__(self):
        return str(self.book)+' : '+str(self.chapter)+' - '+str(self.verse)

