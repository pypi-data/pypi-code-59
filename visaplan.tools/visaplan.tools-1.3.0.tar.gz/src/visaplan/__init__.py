# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
from __future__ import absolute_import
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
