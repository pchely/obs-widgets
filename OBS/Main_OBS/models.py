from django.db import models

class OBS_Model(models.Model):
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Name")
    # name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to="files/")
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=50, null=True);
    subtitle = models.CharField(max_length=50, null=True);