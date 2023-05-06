from django.db import models

# Create your models here.
TAGS = (('Wanderer', 'Wanderer'), ('Enthusiast', 'Enthusiast'), ('Velli', 'Velli'), ('Ugach Firtey', 'Ugach Firtey'))


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField()
    extra_title = models.CharField(max_length=100, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank= True, null=True)
    tags = models.CharField(choices=TAGS,max_length=100, default='Wanderer' )
    
    def __str__(self):
        return f"{self.title}"