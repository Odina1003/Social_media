from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Post(models.Model):
    avatar = models.ImageField(default='post.jpg')
    full_name = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        ordering = ['-full_name']
        
class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(default='post.jpg')
    
    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'