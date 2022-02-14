from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    image_url = models.URLField()

    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
