# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import json

from pathlib import Path
from datetime import datetime


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

setFile = Path("settings.json")
release = "Unknown"
if setFile.exists():
    settings = json.loads(setFile.read_text())
    if isinstance(settings, dict):
        release = settings.get("docVersion", "Unknown")

project = "novelWriter"
copyright = f"2018–{datetime.now().year} Veronica Berglyd Olsen"
author = "Veronica Berglyd Olsen"
version = release


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ["_templates"]
exclude_patterns = []
today_fmt = "%A, %-d %B %Y at %H:%M"
language = "en"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = ""
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_context = {
    "default_mode": "light",
    "build_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
}
html_theme_options = {
    "navbar_align": "content",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button", "theme-switcher"],
    "search_bar_text": "Search text ...",
    "show_toc_level": 2,
    "show_prev_next": True,
    "footer_start": ["copyright", "sphinx-version"],
    "footer_end": ["theme-version", "build-time"],
    "logo": {
        "image_light": "_static/novelwriter-light.png",
        "image_dark": "_static/novelwriter-dark.png",
    },
    "favicons": [{
        "rel": "icon",
        "sizes": "16x16",
        "href": "novelwriter-icon-16.png",
    }, {
        "rel": "icon",
        "sizes": "32x32",
        "href": "novelwriter-icon-32.png",
    }, {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "novelwriter-icon-180.png",
    }],
    "pygment_light_style": "tango",
    "pygment_dark_style": "dracula",
    "icon_links_label": "Quick Links",
    "icon_links": [{
        "name": "Mastodon",
        "url": "https://fosstodon.org/@novelwriter",
        "icon": "fa-brands fa-mastodon",
    }, {
        "name": "GitHub",
        "url": "https://github.com/vkbo/novelwriter",
        "icon": "fa-brands fa-github",
    }, {
        "name": "PyPi",
        "url": "https://pypi.org/project/novelWriter",
        "icon": "fa-solid fa-box",
    }],
}
