from fpdf.structure_tree import PDFObject, StructureTreeBuilder


def test_pdf_object_serialize():
    class Point(PDFObject):
        __slots__ = ("_id", "x", "y")

        def __init__(self, x=0, y=0, **kwargs):
            super().__init__(**kwargs)
            self.x = x
            self.y = y

    class Square(PDFObject):
        __slots__ = ("_id", "top_left", "bottom_right")

        def __init__(self, top_left, bottom_right, **kwargs):
            super().__init__(**kwargs)
            self.top_left = top_left
            self.bottom_right = bottom_right

    point_a = Point(id=1)
    point_b = Point(x=10, y=10, id=2)
    square = Square(top_left=point_a, bottom_right=point_b, id=3)
    pdf_content = (
        point_a.serialize() + "\n" + point_b.serialize() + "\n" + square.serialize()
    )
    assert (
        pdf_content
        == """\
1 0 obj
<<
/X 0
/Y 0
>>
endobj
2 0 obj
<<
/X 10
/Y 10
>>
endobj
3 0 obj
<<
/BottomRight 2 0 R
/TopLeft 1 0 R
>>
endobj"""
    )


def _serialize(struct_builder, first_object_id=1):
    n = first_object_id
    for obj in struct_builder:
        obj.id = n
        n += 1
    return "\n".join(obj.serialize() for obj in struct_builder)


def test_empty_structure_tree():
    struct_builder = StructureTreeBuilder()
    assert (
        _serialize(struct_builder)
        == """\
1 0 obj
<<
/K [2 0 R]
/ParentTree 3 0 R
/Type /StructTreeRoot
>>
endobj
2 0 obj
<<
/K []
/P 1 0 R
/S /Document
/Type /StructElem
>>
endobj
3 0 obj
<<
/Nums []
>>
endobj"""
    )


def test_single_image_structure_tree():
    struct_builder = StructureTreeBuilder()
    struct_builder.add_marked_content(
        1, "/Figure", 0, "Image title", "Image description"
    )
    assert (
        _serialize(struct_builder, first_object_id=3)
        == """\
3 0 obj
<<
/K [4 0 R]
/ParentTree 5 0 R
/Type /StructTreeRoot
>>
endobj
4 0 obj
<<
/K [6 0 R]
/P 3 0 R
/S /Document
/Type /StructElem
>>
endobj
5 0 obj
<<
/Nums [0 [6 0 R]]
>>
endobj
6 0 obj
<<
/Alt <feff0049006d0061006700650020006400650073006300720069007000740069006f006e>
/K [0]
/P 4 0 R
/S /Figure
/T <feff0049006d0061006700650020007400690074006c0065>
/Type /StructElem
>>
endobj"""
    )
