from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        # app_label helps django to recognize your db
        app_label = 'song_book'

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=30)
    lyrics = models.TextField()
    
    #vecinas
    category  = models.ForeignKey(Category , on_delete=models.CASCADE)

    class Meta:
        app_label = 'song_book'

    def __str__(self):
        return self.name