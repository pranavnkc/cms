from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_file_extension
    
class Content(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension], null=True)
    categories = models.TextField()
