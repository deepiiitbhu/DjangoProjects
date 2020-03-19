from django.core.exceptions import ValidationError

def validate_author_email(value):
    if "@" in value:
        return value
    raise ValidationError("Email is not valid")