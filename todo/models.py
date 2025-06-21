from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        tags = ', '.join(tag.name for tag in self.tags.all()[:3])
        status = '✓' if self.is_done else '◻'
        return f"{status} {self.content[:50]}{'...' if len(self.content) > 50 else ''} [Теги: {tags}]"
