from django.db import models

# Create your models here.

class User(models.Model):
    name =  models.CharField(max_length=20)
    school =  models.CharField(max_length=20)


class Post(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)

class Comment(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

