from django.db import models
from multiselectfield import MultiSelectField

class Project(models.Model):
    class DevelopmentTools(models.TextChoices):
        PYTHON = 'Python', 'Python'
        JAVASCRIPT = 'JavaScript', 'JavaScript'
        CSS = 'CSS', 'CSS'
        REACT = 'React', 'React'
        DJANGO = 'Django', 'Django'
        BOOTSTRAP = 'Bootstrap', 'Bootstrap'

    name = models.CharField(max_length=100)
    description = models.TextField()
    tools = models.CharField(max_length=50,choices=DevelopmentTools,default='python',)
    date = models.DateField(blank=True,null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Images(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to='project_images/')



