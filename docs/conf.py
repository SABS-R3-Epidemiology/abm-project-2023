# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ABM project'
copyright = "2023, 'Matthew Ghosh', 'Abbie Evans', 'Tom Reed', 'Yunli Qi', 'Antonio Mastromarino'"
author = "'Matthew Ghosh', 'Abbie Evans', 'Tom Reed', 'Yunli Qi', 'Antonio Mastromarino'"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
