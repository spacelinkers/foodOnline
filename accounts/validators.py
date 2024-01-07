import os
from django.core.exceptions import ValidationError

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] #profile_picture.png
    print(ext)

    valid_extensions = ['.png', '.jpg', '.jepg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extensions. Allowed extensions: ' + str(valid_extensions))
