from django.db import models
from django.utils.text import slugify


class Admission(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    description = models.TextField()
    apply_link = models.URLField()
    last_date = models.DateField()
    pdf = models.FileField(
        upload_to='admissions/pdfs/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']