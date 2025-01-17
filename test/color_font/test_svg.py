from pathlib import Path

from fpdf import FPDF
from test.conftest import LOREM_IPSUM, assert_pdf_equal

HERE = Path(__file__).resolve().parent
FONTS_DIR = HERE.parent / "fonts"


def test_gilbert_color(tmp_path):
    # Gilbert Color - Creative Commons license
    # https://github.com/Fontself/TypeWithPride

    pdf = FPDF()
    pdf.add_font("Gilbert", "", HERE / "Gilbert-Color Bold SVG.otf")

    pdf.add_page()
    pdf.set_font("Gilbert", size=16)
    pdf.multi_cell(w=pdf.epw, text=LOREM_IPSUM.lower(), align="L")
    pdf.ln()
    pdf.multi_cell(w=pdf.epw, text=LOREM_IPSUM.lower(), align="R")
    pdf.ln()
    pdf.multi_cell(w=pdf.epw, text=LOREM_IPSUM.lower(), align="J")

    assert_pdf_equal(pdf, HERE / "svg_gilbert.pdf", tmp_path, generate=True)


def test_twitter_emoji_shaping(tmp_path):
    # Twitter Emoji font - MIT license
    # https://github.com/twitter/twemoji
    pdf = FPDF()
    pdf.add_font("TwitterEmoji", "", FONTS_DIR / "TwitterEmoji.ttf")
    pdf.add_page()
    combined_emojis = "🇫🇷 🇺🇸 🇨🇦 🧑 🧑🏽 🧑🏿"
    pdf.set_font("helvetica", "", 24)
    pdf.cell(text="Emojis without text shaping:", new_x="lmargin", new_y="next")
    pdf.set_font("TwitterEmoji", "", 24)
    pdf.multi_cell(w=pdf.epw, text=combined_emojis, new_x="lmargin", new_y="next")
    pdf.ln()
    pdf.set_font("helvetica", "", 24)
    pdf.cell(text="Emojis with text shaping:", new_x="lmargin", new_y="next")
    pdf.set_font("TwitterEmoji", "", 24)
    pdf.set_text_shaping(True)
    pdf.multi_cell(w=pdf.epw, text=combined_emojis, new_x="lmargin", new_y="next")
    assert_pdf_equal(
        pdf, HERE / "svg_twitter_emoji_shaping.pdf", tmp_path, generate=True
    )
