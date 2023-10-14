"""Top-level initialization for httpstan.

Configures logging and exposes httpstan.__version__.

:license: ISC, see LICENSE for more details.
"""
try:
    import importlib.metadata as import_meta
except:
    import importlib_metadata as import_meta
import logging

logging.getLogger("httpstan").addHandler(logging.NullHandler())

# try-except allows mypy to run without httpstan being installed
try:
    __version__ = import_meta.version("httpstan")
except import_meta.PackageNotFoundError:
    pass
