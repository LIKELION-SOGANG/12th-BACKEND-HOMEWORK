from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.content
