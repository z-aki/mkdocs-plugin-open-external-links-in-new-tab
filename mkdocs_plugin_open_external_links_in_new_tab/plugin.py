from typing import Optional
from lxml.html import fromstring, tostring
from lxml import etree
from mkdocs.plugins import get_plugin_logger
from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config.config_options import Type

log = get_plugin_logger(__name__)


class OpenInNewTabPluginConfig(Config):
    external_extensions = Type(list, default=[".pdf", ".zip"])
    site_url = Optional[Type(str)]


def is_external_link(href, config: OpenInNewTabPluginConfig):
    """
    Checks if href is an external link
    or if it ends in the extensions in the config
    """
    # log.info(config)
    for ext in config.external_extensions:
        if href.endswith(ext):
            return True
    if href.startswith("http") or href.startswith("https"):
        if (
            href.startswith("http://127.0.0.1")
            or href.startswith("https://127.0.0.1")
            or href.startswith(config.site_url)
        ):
            return False
        return True
    return False


class Plugin(BasePlugin[OpenInNewTabPluginConfig]):

    def on_config(self, config):
        self.config.site_url = config["site_url"]

    def on_page_content(self, html, page, config, files):
        """
        Searches for a tags with attribute href
        Adds target="_blank" to any link that is not from 127.0.0.1 or `site_url` config
        """
        if not html:
            # log.debug("No html")
            return html

        content = fromstring(html)
        links = content.xpath("//a[@href]")
        for link in links:
            href = link.get("href", None)
            if href and is_external_link(href, self.config):
                link.set("target", "_blank")
                link.set("rel", "noopener noreferrer")
                link.set("plugin_open_external_links_in_new_tab", "")


        return tostring(content, encoding="unicode")
