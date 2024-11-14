from django.db import models
from django.utils import timezone

class Post(models.Model):


    class Category(models.TextChoices):
        TECHNOLOGY = 'Tech', 'Technology'
        COFFEE = 'Coffee', 'Coffee'
        SPORT = 'Sport', 'Sport'


    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.TECHNOLOGY,
    )

    likes = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.post.title}"