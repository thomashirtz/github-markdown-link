import re
from typing import Union, List


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


def update_text(
        text: Union[str, List[str]],
        new_text: str,
        beginning_flag: str = "<!-- Beginning Flag -->  ",
        end_flag: str = "<!-- End Flag -->  ",
):
    text = text.replace('\r', '')

    if isinstance(text, str):
        lines = text.split('\n')
    else:
        lines = text

    beginning_index = lines.index(beginning_flag)
    end_index = lines.index(end_flag)

    lines[beginning_index + 1:end_index] = new_text
    return '\n'.join(lines)


def update_file(
        file_path: str,
        new_text: str,
        beginning_flag: str = "<!-- Beginning Flag -->  ",
        end_flag: str = "<!-- End Flag -->  ",
):
    with open(file_path, 'rb') as f:
        raw_content = f.read()

    content = update_text(
        text=raw_content.decode(),
        new_text=new_text,
        beginning_flag=beginning_flag,
        end_flag=end_flag,
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
