from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class UserFiles(models.Model):
    """
    this class is for the storing the files
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    title = models.CharField(max_length=150, verbose_name="Title")
    file = models.FileField(upload_to="uploaded-file", verbose_name="File")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    slug = models.SlugField(max_length=250, verbose_name="Slug", null=True, blank=True)
    
    def save(self,*args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super(UserFiles, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.file}"
