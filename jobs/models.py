from django.db import models
from django.utils.text import slugify
from core.models import Category

class Job(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    organization_name = models.CharField(max_length=255)
    short_description = models.TextField()
    full_description = models.TextField()
    eligibility = models.TextField()
    age_limit = models.CharField(max_length=255)
    total_posts = models.CharField(max_length=255)
    application_fee = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    important_dates = models.TextField()
    selection_process = models.TextField()
    how_to_apply = models.TextField()
    apply_link = models.URLField()
    official_website = models.URLField()
    official_notification_pdf = models.FileField(upload_to='jobs/pdfs/', blank=True, null=True)
    featured_image = models.ImageField(upload_to='jobs/images/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
