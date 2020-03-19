from django.contrib import admin

# Register your models here.

from .models import PostModel

class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'content',
        'publish',
        'view_count',
        'publish_date',
        'author_email',
        'updated',
        'timestamp',
        #'new_content',
    ]

    readonly_fields=['updated', 'timestamp']
    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural="Posts"

admin.site.register(PostModel, PostModelAdmin)
