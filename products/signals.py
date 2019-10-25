from django.db.models import signals as sig
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ProductImage
from django.conf import settings
import os
import io
from PIL import Image


@receiver(sig.post_delete, sender=ProductImage)
def remove_image(sender, instance, using, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            print(f'Successfully removed the image at: {instance.image.path}')


@receiver(sig.post_save, sender=ProductImage)
def resize_image(sender, instance, created, raw, using, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            print(f'Image file: {instance.image.path}')
            image = Image.open(os.path.join(
                settings.MEDIA_ROOT, instance.image.name))
            image = image.resize((700, 400), Image.ANTIALIAS)
            image.save(instance.image.path, image.format, quality=100)
            print(f'Successfully resized 700 X 400 image at: {instance.image.path}')
