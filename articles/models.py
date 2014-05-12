from django.db import models
class Article(models.Model):
    headline = models.CharField(max_length=100)
    description = models.CharField(max_length=400,blank=True)#CharField instead of TextField since we want to limit and set a max length
    lastModified = models.DateTimeField()
    articleUrl = models.URLField(max_length=500,blank=True)
    
    def __unicode__(self):
        return self.title
