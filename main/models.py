from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


def uploade_to(instance, filename):
    """
    this function is for preventing the creating another directory inside it
    Args:
        instance (_type_): _description_
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f"uploaded-files/{filename}"


class UserFiles(models.Model):
    """
    this class is for the storing the files
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    title = models.CharField(max_length=150, verbose_name="Title")
    file = models.FileField(upload_to=uploade_to, verbose_name="File")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    slug = models.SlugField(max_length=250, verbose_name="Slug", null=True, blank=True)
    cleaned = models.BooleanField(verbose_name="Cleaned", default=False)
    
    def save(self,*args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super(UserFiles, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.file}"
