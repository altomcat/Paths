import pytest
from path_following.path import PathFollowing, Straight, Curve


def test_default():
    p1 = Curve()
    p2 = Straight()
    p3 = Curve()

    pf = PathFollowing((p1, p2))
    s = pf.segments

    assert s == [p1, p2]

    pf.add(p3)
    p3_id = pf.get_segment_id(p3)

    assert p3_id == 2
