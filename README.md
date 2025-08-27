# Mkdocs Plugin Open External Links In New Tab

This plugin allows you to open external links in a new tab. Adds `target="_blank"` and `"rel"="noopener noreferrer"`  to any link that is not from 127.0.0.1 or `site_url` config.

Certain file extensions (.pdf etc.) to be opened a new tab can also be customized.

The CSS icon before/after the link can also be customized.

> ![image](img_css.jpg)

## Installation

Install the package with pip and `git+https`

<https://pip.pypa.io/en/stable/topics/vcs-support/#git>

```sh
# For major version
pip install mkdocs-plugin-open-external-links-in-new-tab @ git+https://github.com/z-aki/mkdocs-plugin-open-external-links-in-new-tab/@v1
# OR For fixed minor version
pip install mkdocs-plugin-open-external-links-in-new-tab @ git+https://github.com/z-aki/mkdocs-plugin-open-external-links-in-new-tab/@v1.0
# OR For latest develop version
pip install mkdocs-plugin-open-external-links-in-new-tab @ git+https://github.com/z-aki/mkdocs-plugin-open-external-links-in-new-tab/@main
# OR For a fixed commit hash
pip install mkdocs-plugin-open-external-links-in-new-tab @ git+https://github.com/z-aki/mkdocs-plugin-open-external-links-in-new-tab@<commit_hash>
```

## Configuration

```yaml
# mkdocs.yml
site_url: https://<>.github.io
markdown_extensions:
  - attr_list
plugins:
  - mkdocs-plugin-open-external-links-in-new-tab:
      # Optional config. Default values are these:
      external_extensions:
        - ".pdf"
        - ".zip"
```

This plugin also adds `plugin_open_external_links_in_new_tab` attribute to the filtered URLs'
`a` element for easy CSS access.

#### Optional CSS for icon

Add the CSS to customize the icon appearance.

Change `::before` to `::after` if you want to place the icon after the text.

```css
/* docs/stylesheets/extra.css */
/* https://stackoverflow.com/questions/1899772/what-is-the-best-practice-for-showing-an-icon-next-to-text */
.md-typeset a[plugin_open_external_links_in_new_tab]::before {
        content: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);
        margin: 0 3px 0 5px;
}
```

The config for CSS in `mkdocs.yml`:

```yml
extra_css:
  - stylesheets/extra.css
```
