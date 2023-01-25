from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Todo Models
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # set Current time and completed status
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    # User that posted the Todo
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
