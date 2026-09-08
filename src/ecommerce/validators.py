from django.core.exceptions import ValidationError

BLOCKED_WORDS = [
    "cheap",
    "bad"
]  # Example blocked words

def validate_blocked_words(value):
    init_string = f"{value}".lower()
    unique_words = set(init_string.split())
    blocked_words = set(BLOCKED_WORDS)
    invalid_words = unique_words.intersection(blocked_words)
    has_error = len(invalid_words) > 0
    if has_error:
        errors = []
        for i,invalid_word in enumerate(invalid_words):
            msg = f"{invalid_word} is a blocked word."
            errors.append(msg)
        raise ValidationError(errors)
    return value
