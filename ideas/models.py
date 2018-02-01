from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Medium(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Medium, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Idea(models.Model):
    category = models.ForeignKey(Medium, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    inspiration = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title