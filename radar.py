from utils import distance

class Radar:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def scan(self, targets):
        result = []

        for t in targets:
            d = distance(self.x, self.y, t.x, t.y)

            threat = 1 / (d + 1)

            result.append((t, d, threat))

        return result

    def track_closest(self, scan_data):
        return min(scan_data, key=lambda x: x[1])[0]