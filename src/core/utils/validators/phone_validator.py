from django.core.validators import RegexValidator


class PhoneValidator(RegexValidator):
    regex = r'^\+(?:\d{1,3})\s?(?:\d{1,4}[ -]?)?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,9}$'
    message = 'Enter a valid phone number.'
    flags = 0
    code = 'invalid'
