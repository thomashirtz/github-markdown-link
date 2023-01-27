# github-utilities

Collections of tools related to the management of github repositories.

## `get-markdown-link`

Give the URL extension to access the specified anchor by giving the content line.

```python
import github_utilities

raw_string = '## `get-markdown-link`'
url_extension = github_utilities.get_markdown_link(text=raw_string) 
```
