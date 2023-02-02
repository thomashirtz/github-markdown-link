import re


def get_markdown_link(string: str) -> str:
    """Create the link to a markdown header using the raw header.

    Args:
        string: Raw header.

    Returns:
        The header URL suffix.
    """
    # Strip hashes if any
    if string.startswith('#'):
        string = string.split('#')[-1][1:]

    # Remove extra spaces
    string = " ".join(string.split())

    # Remove hyperlinks
    string = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", string)

    # Remove special characters
    string = re.sub(r"[^a-zA-Z0-9\s\u4e00-\u9fff\-]+", "", string)

    # Add hyphens
    string = string.replace(' ', '-')

    # Transform to lowercase
    string = string.lower()

    return string
