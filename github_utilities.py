import re
from collections import defaultdict


def get_markdown_link(text: str) -> str:
    link_text = text.split('#')[-1][1:]
    # Remove extra spaces
    link_text = " ".join(link_text.split())
    # Remove all the links
    link_text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", link_text)
    # Remove the special characters
    link_path = re.sub("[^a-zA-Z0-9\s\u4e00-\u9fff\-]+", "", link_text)
    # Add hyphens and transform to lowercase
    link_path = link_path.replace(' ', '-').lower()
    return link_path
