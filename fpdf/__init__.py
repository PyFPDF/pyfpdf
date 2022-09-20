"""
Root module.
Gives direct access to some classes defined in submodules:

* `fpdf.fpdf.FPDF`
* `fpdf.enums.Align`
* `fpdf.enums.TextMode`
* `fpdf.enums.XPos`
* `fpdf.enums.YPos`
* `fpdf.errors.FPDFException`
* `fpdf.fpdf.TitleStyle`
* `fpdf.prefs.ViewerPreferences`
* `fpdf.template.Template`
* `fpdf.template.FlexTemplate`
"""

import sys

from .enums import Align, TextMode, XPos, YPos
from .errors import FPDFException
from .fpdf import (
    FPDF,
    TitleStyle,
    FPDF_FONT_DIR as _FPDF_FONT_DIR,
    FPDF_VERSION as _FPDF_VERSION,
)
from .html import HTMLMixin, HTML2FPDF
from .prefs import ViewerPreferences
from .template import Template, FlexTemplate
from .text_region import TextColumns
from .deprecation import WarnOnDeprecatedModuleAttributes

FPDF_VERSION = _FPDF_VERSION
"Current fpdf2 version, also available as `__version__`"

FPDF_FONT_DIR = _FPDF_FONT_DIR
"Extra filesystem folder where fpdf2 looks for fonts files, after the current directory"

# Pattern from sir Guido Von Rossum: https://stackoverflow.com/a/72911884/636849
# > a module can define a class with the desired functionality, and then at
# > the end, replace itself in sys.modules with an instance of that class
sys.modules[__name__].__class__ = WarnOnDeprecatedModuleAttributes

__license__ = "LGPL 3.0"

__version__ = FPDF_VERSION

__all__ = [
    # Metadata:
    "__version__",
    "__license__",
    # Classes:
    "FPDF",
    "FPDFException",
    "Align",
    "TextMode",
    "XPos",
    "YPos",
    "Template",
    "FlexTemplate",
    "TitleStyle",
    "ViewerPreferences",
    # Deprecated classes:
    "HTMLMixin",
    "HTML2FPDF",
    # FPDF constants:
    "FPDF_VERSION",
    "FPDF_FONT_DIR",
    "TextColumns",
]

__pdoc__ = {name: name.startswith("FPDF_") for name in __all__}
