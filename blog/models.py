from django.db import models

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ( 'Drf', 'Draft', ),
        ('pub','published'),
                      )


    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3,choices=STATUS_CHOICES)



    def __str__(self):
        return self.title