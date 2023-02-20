from pathlib import Path

import pytest

from fpdf import FPDF
from test.conftest import assert_pdf_equal, LOREM_IPSUM


HERE = Path(__file__).resolve().parent
FONTS_DIR = HERE.parent / "fonts"

TABLE_DATA = (
    ("First name", "Last name", "Age", "City"),
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Angers"),
)
MULTILINE_TABLE_DATA = (
    ("Extract", "Text length"),
    (LOREM_IPSUM[:200], str(len(LOREM_IPSUM[:200]))),
    (LOREM_IPSUM[200:400], str(len(LOREM_IPSUM[200:400]))),
    (LOREM_IPSUM[400:600], str(len(LOREM_IPSUM[400:600]))),
    (LOREM_IPSUM[600:800], str(len(LOREM_IPSUM[600:800]))),
    (LOREM_IPSUM[800:1000], str(len(LOREM_IPSUM[800:1000]))),
    (LOREM_IPSUM[1000:1200], str(len(LOREM_IPSUM[1000:1200]))),
)


def test_table_simple(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table() as table:
        for data_row in TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(pdf, HERE / "table_simple.pdf", tmp_path)


def test_table_with_fixed_col_width(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table() as table:
        table.col_widths = pdf.epw / 5
        for data_row in TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(pdf, HERE / "table_with_fixed_col_width.pdf", tmp_path)


def test_table_with_varying_col_widths(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table() as table:
        table.col_widths = (30, 30, 10, 30)
        for data_row in TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(pdf, HERE / "table_with_varying_col_widths.pdf", tmp_path)


def test_table_with_invalid_col_widths():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pytest.raises(ValueError):
        with pdf.table() as table:
            table.col_widths = (20, 30, 50)
            for data_row in TABLE_DATA:
                with table.row() as row:
                    for datum in data_row:
                        row.cell(datum)


def test_table_with_fixed_row_height(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table(line_height=2.5 * pdf.font_size) as table:
        for data_row in TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(pdf, HERE / "table_with_fixed_row_height.pdf", tmp_path)


def test_table_with_multiline_cells(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table() as table:
        for data_row in MULTILINE_TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(pdf, HERE / "table_with_multiline_cells.pdf", tmp_path)


def test_table_with_multiline_cells_and_fixed_row_height(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table(line_height=2.5 * pdf.font_size) as table:
        for data_row in MULTILINE_TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(
        pdf, HERE / "table_with_multiline_cells_and_fixed_row_height.pdf", tmp_path
    )


def test_table_with_fixed_width(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    with pdf.table(width=150) as table:
        for data_row in TABLE_DATA:
            with table.row() as row:
                for datum in data_row:
                    row.cell(datum)
    assert_pdf_equal(pdf, HERE / "table_with_fixed_width.pdf", tmp_path)
