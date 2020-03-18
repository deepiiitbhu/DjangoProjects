from django.db import models
from django.utils import timezone

# Create your models here.
PUBLISH_CHOICES = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
]
class PostModel(models.Model):
    id  = models.BigAutoField(primary_key=True)
    active  = models.BooleanField(default=True) # it may be empty in the database
    title   = models.CharField(max_length=240, verbose_name='Title Name', unique=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count  = models.IntegerField(default=0)
    publish_datw    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
   
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural="Posts"

    def __unicode__(self):  #pyhton 2
        #return "Blog"
        return self.title
    
    def __str__(self):  #pyhton 3
        #return 'Blog'
        return self.title
   

