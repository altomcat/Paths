
class Path:
    def __init__(self):
        self._vs = 0
        self._ve = 0
        self._xs = 0
        self._ys = 0
        self._xe = 0
        self._ye = 0


class PathFollowing(Path):
    def __init__(self, other_paths):
        if not hasattr(self, '_multiple_path'):
            self._multiple_path = []

        if other_paths is not None:
            self._multiple_path.extend(other_paths)

    def add(self, path_segment):
        self._multiple_path.append(path_segment)

    @property
    def segments(self):
        return self._multiple_path

    def get_segment_id(self, segment):
        return self._multiple_path.index(segment)


class Straight(Path):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Straight segment'


class Curve(Path):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Curve segment'


if __name__ == "__main__":
    p1 = Curve()
    p2 = Straight()
    p3 = Straight()
    pf = PathFollowing((p1, p2))
    print(pf.segments)

    pf.add(p3)

    print(pf.get_segment_id(p3))
