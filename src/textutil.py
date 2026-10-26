"""String helpers."""


def slugify(text):
    """Turn arbitrary text into a URL-safe slug."""
    return text.lower().replace(" ", "-")


def truncate(text, limit):
    """Shorten text to limit characters, appending an ellipsis when cut."""
    if len(text) <= limit:
        return text
    return text[:limit]
