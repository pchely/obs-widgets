from django.db import models

class OBS_Model(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to="files/")
    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name="URL")
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=50, null=True);
    subtitle = models.CharField(max_length=50, null=True);