from django.db import models
from django.utils import timezone

from .validators import validate_author_email



# Create your models here.
PUBLISH_CHOICES = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
]
class PostModel(models.Model):
    id  = models.BigAutoField(primary_key=True)
    active  = models.BooleanField(default=True) # it may be empty in the database
    title   = models.CharField(
        max_length=240, 
        verbose_name='Title Name', 
        unique=True,
        error_messages={
            "unique": "This title is not unique, Pease try again",
            "blank": "this field is not blak, please try again",
        }
        )
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count  = models.IntegerField(default=0)
    publish_date   = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.CharField(max_length=240, validators=[validate_author_email], null=True, blank=True)
    updated           = models.DateTimeField(auto_now=True)
    timestamp         = models.DateTimeField(auto_now_add=True)
   
    


    def __unicode__(self):  #pyhton 2
        #return "Blog"
        return self.title
    
    def __str__(self):  #pyhton 3
        #return 'Blog'
        return self.title
   

