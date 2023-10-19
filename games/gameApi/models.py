from django.db import models

# Create your models here.
class GameModel(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField()
  addedDate = models.DateField()
  categorie = models.CharField(max_length=255)
  plateform = models.CharField(max_length=255)

  def __str__(self):
    return self.title