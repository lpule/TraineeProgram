from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Editor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    editor = models.ForeignKey(Author, related_name='editor', on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
