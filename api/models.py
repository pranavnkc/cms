from django.db import models
from taggit.managers import TaggableManager
from .validators import valid

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
    categories = TaggableManager()
