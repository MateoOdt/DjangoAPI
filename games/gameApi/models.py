from django.db import models
from games.categorie.models import CategoryModel

# Create your models here.
class GameModel(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField()
  addedDate = models.DateField()
  categorie = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=1)
  plateform = models.CharField(max_length=255)

  def __str__(self):
    return self.title
