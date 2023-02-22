# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "novelWriter"
copyright = f"2018–{datetime.now().year} Veronica Berglyd Olsen"
author = "Veronica Berglyd Olsen"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "navbar_align": "left",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button", "theme-switcher"],
    "logo": {
        "image_light": "novelwriter-light.png",
        "image_dark": "novelwriter-dark.png",
        # "image_light": "novelwriter-icon.svg",
        # "image_dark": "novelwriter-icon.svg",
    },
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "novelwriter-icon-16.png",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "novelwriter-icon-32.png",
        },
        {
            "rel": "apple-touch-icon",
            "sizes": "180x180",
            "href": "novelwriter-icon-180.png",
        },
    ],
    "pygment_light_style": "tango",
    "pygment_dark_style": "monokai",
    "icon_links_label": "Quick Links",
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@novelwriter",
            "icon": "fa-brands fa-mastodon",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/vkbo/novelwriter",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPi",
            "url": "https://pypi.org/project/novelWriter",
            "icon": "fa-solid fa-box",
        },
    ],
}
