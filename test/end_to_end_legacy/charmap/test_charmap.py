"""Charmap Test Case

This module contains the test case for the Charmap Test. It prints the first
999 characters of the unicode character set with a unicode ttf font, and
verifies the result against a known good result.

This test will complain that some of the values in this font file are out of
the range of the C 'short' data type (2 bytes, 0 - 65535):
  fpdf/ttfonts.py:671: UserWarning: cmap value too big/small:
and this seems to be okay.
"""
import os
from glob import glob

import pytest

import fpdf
from fpdf.ttfonts import TTFontFile
from test.utilities import assert_pdf_equal, relative_path_to


class MyTTFontFile(TTFontFile):
    """MyTTFontFile docstring

    I clearly have no idea what this does. It'd be great if this class were
    even a little bit better documented, so that it would be clearer what this
    test is testing, otherwise this test isn't clearly testing one class or the
    other.

    """

    def getCMAP4(self, unicode_cmap_offset, glyphToChar, charToGlyph):
        TTFontFile.getCMAP4(self, unicode_cmap_offset, glyphToChar, charToGlyph)
        self.saveChar = charToGlyph

    def getCMAP12(self, unicode_cmap_offset, glyphToChar, charToGlyph):
        TTFontFile.getCMAP12(self, unicode_cmap_offset, glyphToChar, charToGlyph)
        self.saveChar = charToGlyph


class TestCharmap:
    @pytest.mark.parametrize(
        "fontpath",
        ["DejaVuSans.ttf", "DroidSansFallback.ttf", "Roboto-Regular.ttf", "cmss12.ttf"],
    )
    def test_first_999_chars(self, fontpath):
        fontname = os.path.splitext(fontpath)[0]
        fontpath = relative_path_to(fontpath)

        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.add_font(fontname, fname=fontpath, uni=True)
        pdf.set_font(fontname, size=10)

        ttf = MyTTFontFile()
        ttf.getMetrics(fontpath)

        # Create a PDF with the first 999 charters defined in the font:
        for counter, character in enumerate(ttf.saveChar, 0):
            pdf.write(8, f"{counter:03}) {character:03x} - {character:c}")
            pdf.ln()
            if counter >= 999:
                break

        assert_pdf_equal(pdf, f"charmap_first_999_chars-{fontname}.pdf")

    def tearDown(self):
        for pkl_filepath in glob(relative_path_to("*") + "*.pkl"):
            os.remove(pkl_filepath)
