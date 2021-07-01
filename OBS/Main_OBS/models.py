from django.db import models

class OBS_Model(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to="files/")
    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reversed("widget", kwargs={"name_slug":self.slug})