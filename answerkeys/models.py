from django.db import models
from django.utils.text import slugify

class AnswerKey(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    description = models.TextField()
    download_link = models.URLField()
    pdf = models.FileField(upload_to='answerkeys/pdfs/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
