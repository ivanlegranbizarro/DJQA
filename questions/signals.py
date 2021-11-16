from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Question
from django.utils.text import slugify


@receiver(pre_save, sender=Question)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
