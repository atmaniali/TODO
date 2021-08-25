from django.db import models

# Create your models here.
# Todo models
class Todo(models.Model):
    titre       = models.CharField(max_length=100)
    description = models.TextField()
    is_doing    = models.BooleanField(default = False)

    def __str__(self):
        return self.titre
