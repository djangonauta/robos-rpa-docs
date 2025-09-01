# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import tomllib

project = "Robôs RPA"
copyright = "2025, Igor Carvalho"
author = "Igor Carvalho"
with open("../pyproject.toml", "rb") as f:
    config = tomllib.load(f)
    release = config["project"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "pt_BR"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["libs/fancybox/css/fancybox.css", "css/main.css"]
html_js_files = ["libs/fancybox/js/fancybox.umd.js", "js/main.js"]
