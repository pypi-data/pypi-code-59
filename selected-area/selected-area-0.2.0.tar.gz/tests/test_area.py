import pytest
from selected_area import Segment, SelectedArea


def test_segments():
    """
    https://postimg.cc/HcH38dt1
    """
    area = SelectedArea((1, 2), (4, 4))               # diagonal AC

    segment1 = Segment((2, 1.5), (4.5, 3.5))          # EF
    segment2 = Segment((1, 1.5), (1, 4.5))            # GH
    segment3 = Segment((3, 1), (4.5, 2.5))            # IJ
    segment4 = Segment((4, 1), (5, 3))                # KL
    segment5 = Segment((1.5, 1), (3.5, 4.5))          # MN
    segment6 = Segment((1.73, 3.19), (2.5, 3.5))      # OP
    segment7 = Segment((0.28, 2.93), (2.42, 3.82))    # QR
    segment8 = Segment((2, 0.5), (5.5, 0.5))          # ST
    segment9 = Segment((5.5, 2), (5.5, 4))            # UV
    segment10 = Segment((2, 1), (5.63, 1.8))          # WZ

    assert area.contains(segment1)
    assert area.contains(segment2)
    assert area.contains(segment3)
    assert not area.contains(segment4)
    assert area.contains(segment5)
    assert area.contains(segment6)
    assert area.contains(segment7)
    assert not area.contains(segment8)
    assert not area.contains(segment9)
    assert not area.contains(segment10)
    assert repr(segment4) == 'Segment(p1=Point(x=4, y=1), p2=Point(x=5, y=3))'


def test_exceptions():
    with pytest.raises(TypeError):
        Segment([1, 2], [2, 3])
    with pytest.raises(ValueError):
        Segment((1, 2, 3), (2, 3))
