from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content