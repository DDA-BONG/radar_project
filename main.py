import time
from radar import Radar
from target import Target

radar = Radar(0, 0)

targets = [
    Target("A", 50, 20),
    Target("B", 100, 40),
    Target("C", 50, 130)
]

tick = 0

while True:
    print("\n======================")
    print(f"RADAR SCAN TICK {tick}")
    print("======================")

    for t in targets:
        t.move() #랜덤 이동

    scan = radar.scan(targets)
    tracking = radar.track_closest(scan)

    for t, d, th in scan:
        mark = " <-- TRACKING" if t == tracking else ""
        print(f"{t.name} | pos=({t.x},{t.y}) | dist={int(d)} | threat={th:.2f}{mark}")

    tick += 1
    time.sleep(1)