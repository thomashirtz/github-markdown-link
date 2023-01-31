import pytest
from github_utilities import get_markdown_link


# Taken from https://github.com/thomashirtz/awesome-chinese-learning
parameter_list = [
    ('测试', '测试'),
    ('# 测试', '测试'),
    ('## 测试', '测试'),
    ('### 测试', '测试'),
    ('### [Youku (优酷)](https://www.youku.com/)', 'youku-优酷'),
    ('### /r/ChineseLanguage ([Reddit](https://www.reddit.com/r/ChineseLanguage/) & [Discord](https://discord.com/invite/chineselanguage))', 'rchineselanguage-reddit--discord'),
]


@pytest.mark.parametrize("raw_string, expected_url", parameter_list)
def test_get_markdown_link(raw_string, expected_url):
    assert get_markdown_link(raw_string) == expected_url
