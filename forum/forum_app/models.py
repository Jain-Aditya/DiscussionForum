from django.db import models

# Create your models here.
class Category(models.Model):
    category_text = models.CharField(max_length=200)
    def __str__(self):
        return self.category_text

class Discussion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discussion_text = models.CharField(max_length=1500)
    def __str__(self):
        return self.discussion_text    
