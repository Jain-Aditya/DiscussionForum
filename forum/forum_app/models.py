from django.db import models
# Create your models here.
class Category(models.Model):
    category_text = models.CharField(max_length=200)
    def __str__(self):
        return self.category_text

class Discussion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discussion_text = models.CharField(max_length=1500)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.discussion_text    

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1500)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.comment_text